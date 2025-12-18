import json
import os

def save_data(data,filename="data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f ,indent= 4)
            
def load_data(filename="data.json"):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r+") as f:
            return json.load(f)
        
        