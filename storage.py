## This is the storage manager  file  for the expense_manager app which user the json data system 

# progect import


# module import 
import json
from pathlib import Path

path = Path("expanse_tracker_DB.json")

def get_data() -> list: 
    if path.exists():
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    return []
    
def save_data(expanse_list) -> bool :
    with path.open("w" , encoding="utf-8") as file:
        json.dump(expanse_list, file , indent= 2)
        return True

    

        