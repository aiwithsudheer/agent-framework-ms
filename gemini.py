
import asyncio
import os
from typing import Any, AsyncIterable

from agent_framework import (
    ChatClientProtocol,
    ChatMessage,
    ChatResponse,
    AgentRunResponse,
    AgentRunResponseUpdate,
    Role,
    TextContent,
)
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()



class GeminiChatClient:
    """
    A chat client that uses the Google Gemini API to generate responses.

    This class implements the ChatClientProtocol and provides methods for getting
    both streaming and non-streaming responses from a specified Gemini model.
    """

    def __init__(self, model: str) -> None:
        """
        Initializes the GeminiChatClient.

        :param model: The name of the Gemini model to use (e.g., "gemini-1.5-flash").
        """
        self.model = model
        API_KEY = os.environ.get("GEMINI_API_KEY")
        self.client = genai.Client(api_key=API_KEY)

    @property
    def additional_properties(self) -> dict[str, Any]:
        return {}

    async def get_response(
        self, messages: list[ChatMessage], **kwargs
    ):
        """
        Gets a non-streaming response from the Gemini API.

        :param messages: A list of messages in the conversation.
        :param kwargs: Additional keyword arguments for the Gemini API.
        :return: A ChatResponse object containing the assistant's reply.
        """
        # Convert the agent framework's message format to the Gemini API's format.
        response = await self.client.aio.models.generate_content(
            model=self.model, 
            contents=[
                # Gemini expects a list of dictionaries with 'role' and 'parts'.
                types.ContentDict(
                    role="model" if msg.role == Role.ASSISTANT else "user", 
                    parts=[types.Part(text=content.text)]
                ) for msg in messages for content in msg.contents
            ]
        )
        response_message = ChatMessage(role=Role.ASSISTANT, content=response.text)
        return ChatResponse(messages=[response_message], response_id=str(response.response_id))

    def get_streaming_response(
        self, messages: list[ChatMessage], **kwargs
    ):
        """
        Gets a streaming response from the Gemini API.

        :param messages: A list of messages in the conversation.
        :param kwargs: Additional keyword arguments for the Gemini API.
        :return: An async iterable of AgentRunResponseUpdate objects for streaming.
        """

        async def _stream():
            # Convert the agent framework's message format to the Gemini API's format.
            async for chunk in await self.client.aio.models.generate_content_stream(
                model=self.model,
                contents=[
                    types.ContentDict(
                        role="model" if msg.role == Role.ASSISTANT else "user", 
                        parts=[types.Part(text=content.text)]
                    ) for msg in messages for content in msg.contents
                ],
            ):
                # Yield each chunk of text as it is received from the API.
                yield AgentRunResponseUpdate(
                    contents=[TextContent(text=chunk.text)],
                    role=Role.ASSISTANT,
                )

        return _stream()

 # Verify the instance satisfies the protocol
client = GeminiChatClient(model="gemini-2.5-flash")
isinstance(client, ChatClientProtocol)