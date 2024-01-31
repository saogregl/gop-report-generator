# # Now we need to read the json files and get the ids from each category
# # We will use the ids to search for the occurrences
# # Path: main.py
import json


def get_tests():
    # # lista de categories
    category = "teste"
    # # lista de ids
    ids = []

    # # Loop through the categories
    # Open the json file
    # The file is expected to be in the ./export/gop_tests folder
    directory = "./export/gop_tests"
    with open("{}/{}.json".format(directory, category), "r") as f:
        # Load the json file
        data = json.load(f)
        # Loop through the data
        for item in data:
            # Append the id to the ids list
            ids.append({
                "id": item["id"],
                "descricao": item["descricao"],
                "maquinaID": {
                    "id": item["maquina"]["id"],
                    "nome": item["maquina"]["nome"],
                },
                "projetoID": {
                    "id": item["maquina"]["projeto"]["id"],
                    "descricao": item["maquina"]["projeto"]["descricao"],
                }
            })
    return ids # Return the ids




