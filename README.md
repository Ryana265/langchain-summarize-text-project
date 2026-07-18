# LangChain Text Summarizer

A simple AI-powered text summarization project built with **LangChain** and **Ollama**. This project demonstrates how to use prompt templates and local large language models (LLMs) to generate concise summaries from long pieces of text.

## Features

* Summarizes long-form text into short, readable summaries.
* Uses LangChain's `PromptTemplate` for reusable prompts.
* Runs completely locally using Ollama (no OpenAI or Gemini API required).
* Beginner-friendly project for learning LangChain fundamentals.

## Tech Stack

* Python 3.13+
* LangChain
* LangChain Ollama
* Ollama
* UV (Python package manager)

## Project Structure

```text
.
├── main.py          # Main application
├── pyproject.toml   # Project dependencies
├── uv.lock          # Dependency lock file
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd langchain-text-summarizer
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Install Ollama

Download and install Ollama from:

https://ollama.com

### 4. Download a model

For example:

```bash
ollama pull llama3.2
```

### 5. Run the Ollama server

```bash
ollama serve
```

If Ollama is already running, you can skip this step.

### 6. Run the project

```bash
uv run main.py
```

## Example Workflow

1. Provide a block of text.
2. LangChain inserts the text into a prompt template.
3. The prompt is sent to the local Ollama model.
4. The model returns a concise summary.

## Example Prompt

```text
Summarize the following information:

{information}
```

## Learning Objectives

This project demonstrates:

* LangChain Prompt Templates
* LangChain Expression Language (LCEL)
* Runnable Chains
* Local LLM integration with Ollama
* Prompt engineering basics

## Future Improvements

* Upload and summarize PDF files
* Summarize web articles from URLs
* Support multiple languages
* Stream responses
* Build a Streamlit or React frontend
* Add conversation memory
* Add output parsers for structured summaries

## License

This project is intended for educational and learning purposes.
