def generate_docs(insights):
    doc = f"# {insights['title']}\n\n"
    doc += f"**Summary:** {insights['summary']}\n\n"
    doc += "## Components\n\n"
    for comp in insights.get("components", []):
        doc += f"- {comp}\n"
    doc += f"\n**LLM Summary:**\n{insights.get('llm_summary', 'N/A')}"
    return doc
