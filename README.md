# Python Agent Framework with Gemini Client

This project demonstrates how to extend the `agent-framework` by creating a custom chat client for Google's Gemini large language models. It includes a working `GeminiChatClient` that implements the `ChatClientProtocol` and an example script showing how to use it.

## Features

- **Custom Chat Client**: Implements `GeminiChatClient` to connect to the Google Gemini API.
- **Protocol Compliant**: The client correctly implements the `ChatClientProtocol`.
- **Streaming and Non-Streaming**: Supports both standard request-response and streaming responses.
- **Easy to Use**: A simple `main.py` script demonstrates how to instantiate and run an agent with the custom client.

## Prerequisites

- Python 3.8+
- A Google Gemini API Key. You can get one from Google AI Studio.

## Setup

1.  **Clone the repository or download the files.**

2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    or
    ```bash
    uv sync
    ```

3.  **Create a `.env` file:**

    In the root directory of the project, create a file named `.env`.

4.  **Add your API Key to the `.env` file:**

    Open the `.env` file and add your Google Gemini API key like this:

    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

## Usage

Once the setup is complete, you can run the example script:

```bash
python main.py
```
or
```bash
uv run main.py
```

## Output

The script will execute two interactions with the Gemini model:

1.  A **non-streaming** request for the "meaning of life," printing the complete JSON response at the end.
2.  A **streaming** request for the "purpose of life," printing the response text to the console as it is generated.

### Expected Output

The output will look something like this:

```
Agent response: {"messages": [{"role": "assistant", "contents": [{"text": "The meaning of life is a profound question that has been debated by philosophers, theologians, and thinkers for centuries..."}]}], "response_id": "..."}
Agent streaming response:
The purpose of life, much like its meaning, is a deeply personal and philosophical question...
```

## Code Structure

```
├── main.py                 # Main entry point, demonstrates agent usage.
├── gemini.py               # Contains the GeminiChatClient implementation.
├── requirements.txt        # Project dependencies.
├── .env                    # (You create this) For storing environment variables.
└── README.md               # This file.
```

- **`main.py`**: This script shows how to instantiate `ChatAgent` with the custom `GeminiChatClient` and run it in both non-streaming (`agent.run`) and streaming (`agent.run_stream`) modes.
- **`gemini.py`**: This module contains the `GeminiChatClient` class. It handles the logic for communicating with the Google Gemini API, including message formatting and handling both single and streaming responses.

---
