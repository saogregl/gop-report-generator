import os
import requests
import json
import concurrent.futures
from dotenv import load_dotenv
from src.query import query_gop
from src.tests import get_tests
from src.login import login

def process(test): 
    ocorrencias = []
    searchTerm = query_gop(test["projetoID"]["id"], test["maquinaID"]["id"], test["id"])
    print(searchTerm)
    s = login()
    resp = requests.get(
        url="https://gop-homol.jacto.srv.br/ocorrencia/getOcorrenciasJSON?{searchTerm}".format(
            searchTerm=searchTerm
        ),
        cookies=s.cookies.get_dict(),
    )

    response_ocorrencias = {
        "id": test["id"],
        "descricao": test["descricao"],
        "maquinaID": {
            "id": test["maquinaID"]["id"],
            "nome": test["maquinaID"]["nome"],
        },
        "projetoID": {
            "id": test["projetoID"]["id"],
            "descricao": test["projetoID"]["descricao"],
        },
        "ocorrencias": resp.json(),
    }

    ocorrencias.append(response_ocorrencias)

    # Save the response as a json file
    with open("./export/gop_tests/{searchTerm}.json".format(searchTerm=test["id"]), "w",encoding='utf8') as f:
        f.write(json.dump(response_ocorrencias, f, ensure_ascii=False))


# # Using ThreadPoolExecutor to execute the loop in parallel
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = [executor.submit(process, test) for test in ids]

# # Wait for all tasks to complete
# concurrent.futures.wait(futures)

# The 'ocorrencias' list now contains the processed results
def run_extraction():
    ids = get_tests()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process, test) for test in ids]
    
    concurrent.futures.wait(futures)
    print("Extraction completed.")
