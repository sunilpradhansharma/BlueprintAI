from graphviz import Digraph

def generate_diagram(insights):
    dot = Digraph()
    for comp in insights.get("components", []):
        dot.node(comp)
    for i in range(len(insights.get("components", [])) - 1):
        dot.edge(insights["components"][i], insights["components"][i+1])
    file_path = "app/static/diagram.png"
    dot.render(filename="diagram", directory="app/static", format="png", cleanup=True)
    return file_path
