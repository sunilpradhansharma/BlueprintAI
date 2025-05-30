# BluePrintAI

BluePrintAI is an AI-powered tool that automatically generates:

- 📄 Structured documentation (Markdown, JSON, HTML)
- 🧱 Architecture diagrams
- 🔄 Flowcharts
- 📊 Visual insights

## 🔧 Features

- Supports Web, File, and API data sources.
- Summarizes using LangChain + OpenAI.
- Renders diagrams with Graphviz.
- FastAPI for interactive generation API.

## 📦 Installation

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🚀 API

```http
POST /generate-docs
```

Payload: Upload file (.json, .yaml, .csv, .html)

Returns: Markdown + Diagram Path
