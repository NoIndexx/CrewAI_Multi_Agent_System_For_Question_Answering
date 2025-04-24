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

## Next Steps for Development

This project has great potential for expansion and improvement. Here are some suggested next steps:

### Adding New Knowledge Bases

- **Local Document Storage**: Implement a local vector database (like Chroma or FAISS) to store documents for private data retrieval
- **SQL Integration**: Add capability to query SQL databases for structured data answers
- **PDF Processing**: Add functionality to upload and process PDF documents for domain-specific knowledge
- **Custom API Connectors**: Develop connectors to proprietary data sources or services

### Using Alternative LLM Models

- **Local Models**: Integrate with local LLM runners like Ollama or LM Studio for private deployment
- **Specialized Models**: Test with domain-specific models (legal, medical, scientific) for targeted applications
- **Multi-Modal Integration**: Add support for models that can process images or audio as part of the input
- **Model Fallbacks**: Implement fallback mechanisms to handle API limits or service outages

### Prompt Engineering Improvements

- **Few-Shot Examples**: Add few-shot examples to improve the quality of responses
- **Custom Instructions**: Develop domain-specific instructions for specialized use cases
- **Chain-of-Thought**: Implement chain-of-thought prompting for more complex reasoning tasks
- **Prompt Templates**: Create a library of prompt templates for different question types

### UI and UX Enhancements

- **Chat History**: Add a conversation history feature to reference previous questions and answers
- **Interactive Citations**: Make sources clickable and more interactive
- **User Feedback Loop**: Implement a rating system to gather feedback on answer quality
- **Advanced Filtering**: Add options to filter sources by type, date, or relevance

### Evaluation and Testing

- **Benchmarking**: Create a benchmark dataset to evaluate system performance
- **A/B Testing**: Build infrastructure to test different prompt strategies or models
- **Monitoring**: Add logging and monitoring tools to track usage patterns and errors

Each of these improvements can be implemented incrementally, gradually enhancing the system's capabilities while maintaining its core functionality. 