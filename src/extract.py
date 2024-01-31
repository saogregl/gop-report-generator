import os
import requests
from src.login import login


def extract_gop():
    """
    Extracts data from the GOP website for the specified categories and saves the response as JSON files.
    The categories are: "projeto", "maquina", "teste".
    The results are all items in those categories.

    Returns:
        None
    """
    categories = ["projeto", "maquina", "teste"]
    # lista de categories
    s = login()

    export_path = "./export/gop_tests"
    os.makedirs(export_path, exist_ok=True)  # This creates the directory if it doesn't exist

    for searchTerm in categories:
        response_cat = requests.get(
            url="http://gop-homol.jacto.srv.br/{}/busca/".format(
                searchTerm
            ),
            cookies=s.cookies.get_dict(),
        )
        with open("{}/{}.json".format(export_path, searchTerm), "w") as f:
            f.write(response_cat.text)
