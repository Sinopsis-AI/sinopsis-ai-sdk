# Official Sinopsis AI SDK for Python

This is the official Python SDK for interacting with [Sinopsis AI](https://www.sinopsisai.com), designed to simplify the process of logging user prompts and responses, and managing conversation data.

## Features

- **Easy Integration**: Quickly integrate Sinopsis AI into your Python applications.
- **Session Management**: Start, manage, and end sessions with ease.
- **Conversation Logging**: Log user prompts and assistant responses with timestamps.
- **API Interaction**: Communicate with the Sinopsis AI backend API seamlessly.
- **Error Handling**: Robust error handling with retry logic for network requests.

## Installation

You can install the package using pip:

```bash
pip install sinopsis-ai

## Configuration

```bash
from sinopsis_ai import SinopsisAI

# Initialize the SDK with your API key
api_key = "your_api_key_here"
client = SinopsisAI(api_key)
