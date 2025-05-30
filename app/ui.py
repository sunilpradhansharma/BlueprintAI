import gradio as gr
from app.core.parser import parse_input
from app.core.processor import process_data
from app.core.langchain_prompt import enrich_with_llm
from app.core.doc_gen import generate_docs
from app.core.diagram_gen import generate_diagram

def generate_docs_from_file(file):
    content = file.read()
    parsed = parse_input(content)
    insights = process_data(parsed)
    enriched = enrich_with_llm(insights)
    doc = generate_docs(enriched)
    diagram_path = generate_diagram(enriched)
    return doc, diagram_path

iface = gr.Interface(
    fn=generate_docs_from_file,
    inputs=gr.File(type="binary"),
    outputs=["textbox", "image"],
    title="BluePrintAI - AI-powered Doc Generator",
    description="Upload a file (JSON, YAML, CSV, HTML) to generate documentation and a system diagram"
)

if __name__ == "__main__":
    iface.launch()
