import logging
import json
import os
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

def save_to_json(data, filename):
    path = os.path.normpath(os.path.join(os.getcwd(), "output"))
    os.makedirs(path, exist_ok=True)
    full_path = os.path.normpath(os.path.join(path, f"{filename}.json"))
    try:
        with open(full_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logging.info("Successfully saved data to extracted.json")
    except Exception as e:
        logging.error(f"Error saving to JSON: {e}")