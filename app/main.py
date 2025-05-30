from fastapi import FastAPI, UploadFile, File
from app.core.parser import parse_input
from app.core.processor import process_data
from app.core.doc_gen import generate_docs
from app.core.diagram_gen import generate_diagram
from app.core.langchain_prompt import enrich_with_llm

app = FastAPI()

@app.post("/generate-docs")
async def generate(file: UploadFile = File(...)):
    raw_data = await file.read()
    parsed = parse_input(raw_data)
    insights = process_data(parsed)
    enriched = enrich_with_llm(insights)
    doc = generate_docs(enriched)
    diagram = generate_diagram(enriched)
    return {"documentation": doc, "diagram": diagram}
