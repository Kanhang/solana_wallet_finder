import json


# function to add to JSON
def write_json(addr, filename='solana_wallet.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        obj = {
            "isConnected": True,
            "address": addr,
            "balance": None,
            "isDisabled": False,
            "type": "SOL",
            "phrase": "-=--=-=-=-",
            "label": None,
            "ens": None,
            "group": ["Personal Group"]
          }
        # Join new_data with file_data inside emp_details
        file_data.append(obj)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)
        file.close()

    # python object to be appended



public_keys_file = open("logfile.txt",'r')
public_keys = public_keys_file.readlines()
for key in public_keys:
    write_json(key.strip())
public_keys_file.close()

