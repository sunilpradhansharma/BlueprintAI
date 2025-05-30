from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
model = ChatOpenAI(temperature=0.3)

template = PromptTemplate(
    template="""You are an expert system architect. Based on the components: {components}, provide a concise summary of what the system likely does.""",
    input_variables=["components"]
)

def enrich_with_llm(insights):
    prompt = template.invoke({"components": ", ".join(insights.get("components", []))})
    result = model.invoke(prompt)
    insights["llm_summary"] = result.content
    return insights
