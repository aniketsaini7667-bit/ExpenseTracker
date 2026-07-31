## This is the storage manager  file  for the expense_manager app which user the json data system 

# progect import


# module import 
import json
import csv
from pathlib import Path

pathjson = Path("expense_tracker_DB.json")
pathcsv = Path("expense_tracker_DB.csv")

def get_data() -> list: 
    if pathjson.exists():
        try :
            with pathjson.open("r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except Exception :
            return []
    return []
    
def save_data(expense_list) -> bool :
    with pathjson.open("w" , encoding="utf-8") as file:
        json.dump(expense_list, file , indent= 2)
        return True

    
def export_to_csv(headerrow,bodyrow) -> bool:
    try :
        with pathcsv.open("w",newline="",encoding="utf-8") as file:
            export = csv.writer(file)
            export.writerow(headerrow)
            export.writerows(bodyrow)
        return True
    except Exception :
        return False