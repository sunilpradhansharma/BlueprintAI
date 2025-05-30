def process_data(data):
    return {
        "title": "Generated System",
        "components": list(data.keys()) if isinstance(data, dict) else [],
        "summary": f"Processed {len(data)} items"
    }
