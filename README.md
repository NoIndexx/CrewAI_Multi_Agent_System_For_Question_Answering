# AI Question Answering System

This application demonstrates an advanced AI-powered question answering system that provides concise, context-aware answers by retrieving relevant information and using large language models.

## Overview

The AI Question Answering System uses large language models (LLMs) to:

- Find relevant information from reliable sources
- Process and analyze retrieved data
- Generate accurate and concise answers to user questions
- Provide sources for the information used in answers

## Prerequisites

- Python 3.11.11 (required)
- Pip (Python package manager)

## Setup

1. Make sure the `.env` file contains all necessary API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the application

Run the following command in the terminal:

```
streamlit run app.py
```

This will start the Streamlit server and automatically open the application in your default browser.

## Usage

1. Enter your question in the text field (a default question about recent Pope news is provided)
2. Click the "Get Answer" button
3. Wait while the AI agents work on finding information and generating an answer
4. The results will be displayed on the page:
   - First, the AI-generated answer to your question
   - Below the answer, a list of sources where the information was found

## Project Structure

- `app.py`: Streamlit application with the AI Question Answering interface
- `agents.yaml`: Configurations for specialized AI agents
- `tasks.yaml`: Task configurations for information retrieval and answer generation
- `.env`: Environment variables file (API keys) 