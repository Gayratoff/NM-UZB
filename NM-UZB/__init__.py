import json
import re
def name_search(name):
    c = 0
    file_path = "words.json"
    text = ""
    with open(file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)
    for item in json_data:
        if re.search(str(name), item["word"], re.IGNORECASE):
            text += f"{item['word']} - {item['example']}\n\n"
            if text.count('-') > 10:
                return text

    return text
