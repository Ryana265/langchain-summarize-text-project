# LangChain Text Summarizer

A simple AI-powered text summarization project built with **LangChain** and **Ollama**, powered by Google's **Gemma** model. This project demonstrates how to use prompt templates and a locally running LLM to generate concise summaries from long pieces of text—without relying on cloud-based AI APIs.

## Features

* Summarizes long-form text into concise, easy-to-read summaries.
* Uses LangChain's `PromptTemplate` for reusable prompt creation.
* Runs locally with Ollama and the Gemma model.
* No OpenAI or Gemini API key required.
* Beginner-friendly project for learning LangChain fundamentals.

## Tech Stack

* Python
* LangChain
* LangChain Ollama
* Ollama
* Gemma
* UV

## Project Structure

```text
.
├── main.py
├── pyproject.toml
├── uv.lock
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

### 4. Pull the Gemma model

```bash
ollama pull gemma3
```

> If you're using a different Gemma version (for example `gemma3:4b`), update the model name in your code accordingly.

### 5. Start Ollama

```bash
ollama serve
```

### 6. Run the application

```bash
uv run main.py
```

## How It Works

1. The user provides a block of text.
2. LangChain inserts the text into a prompt template.
3. The prompt is sent to the local Gemma model through Ollama.
4. Gemma generates a concise summary.
5. The summarized output is displayed in the terminal.

## Example Prompt

```text
Summarize the following information in a few sentences.

{information}
```

## Learning Outcomes

This project demonstrates:

* Prompt Templates
* LangChain Expression Language (LCEL)
* Runnable Chains
* Local LLMs with Ollama
* Integrating the Gemma model with LangChain
* Basic prompt engineering

## Future Improvements

* Summarize PDF documents
* Summarize web pages
* Add a Streamlit or React frontend
* Support multiple LLMs
* Add conversation memory
* Generate structured summaries using output parsers

## License

This project is created for educational and learning purposes.
