import asyncio
from agent_framework import ChatAgent
from gemini import GeminiChatClient


async def main():
    """
    An example of how to use the ChatAgent with the GeminiChatClient.
    """
    # The ChatAgent is a context manager that handles the lifecycle of the agent.
    async with (
        ChatAgent(
            # Instantiate the GeminiChatClient with a specific model.
            chat_client=GeminiChatClient(
                model="gemini-2.5-flash",
            ),
            instructions="You are a friendly and helpful assistant."
        ) as agent
    ):
        # --- Non-streaming example ---
        # The `run` method sends the message and waits for the full response.
        response = await agent.run("What is the meaning of life?")
        print("Agent response:", response.to_json())
        # --- Streaming example ---
        # The `run_stream` method returns an async generator that yields updates as they arrive.
        print("Agent streaming response:")
        async for update in agent.run_stream("What is the purpose of life?"):
            # Each update may contain a piece of the response text.
            if update.text:
                print(update.text, end="")
        print()


if __name__ == "__main__":
    asyncio.run(main())