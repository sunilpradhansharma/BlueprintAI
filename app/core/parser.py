import json
import yaml
import pandas as pd
from bs4 import BeautifulSoup

def parse_input(content):
    try:
        return json.loads(content)
    except:
        try:
            return yaml.safe_load(content)
        except:
            try:
                df = pd.read_csv(content)
                return df.to_dict()
            except:
                soup = BeautifulSoup(content, 'html.parser')
                return {"text": soup.get_text()}
