
import json
import pandas as pd
import os
import sys
from datetime import datetime
from openpyxl import load_workbook
import xlsxwriter
import flatdict


def to_excel():
    all_data = []

    def get_modulos(ocorrencia):
        modulos = ''
        if ocorrencia.get("modulos") is None:
            return modulos
        for modulo in ocorrencia.get("modulos"):
            modulos = modulos + " " + (modulo.get("modulo")["descricao"])
        return modulos

    # Loop through the JSON files in the "gop_tests" folder
    # We need to go to the parent folder first

    folder_path = "./export/gop_tests"

    for filename in os.listdir(folder_path):
        if filename.endswith(".json") and filename != "teste.json" and filename != "maquina.json" and filename != "projeto.json": # TODO: Remove this condition
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf8") as f:
                data = json.load(f)
                if data["ocorrencias"] != {'string': 'Vazio'}: 
                    for ocorrencia in data["ocorrencias"]: 
                        ocorrencia_flat = flatdict.FlatDict(ocorrencia, delimiter='.')
                        ocorrencia_flat = flatdict.FlatDict(ocorrencia_flat, delimiter='.')
                        modulo_description = get_modulos(ocorrencia_flat)
                        status = ocorrencia_flat.get("lastStatus")
                        nivelFalha = ocorrencia_flat.get("nivelFalha.descricao")
                        dataTratada = ocorrencia_flat.get("dataTratada")
                        id_ocorrencia = ocorrencia_flat.get("id")
                        descricaoOcorrencia = ocorrencia_flat.get("descricao")

                        # 
                        ocorrencia_data = {
                            "projetoDescricao": data["projetoID"]["descricao"],
                            "maquinaNome": data["maquinaID"]["nome"],
                            "descricaoTeste": data["descricao"],
                            "idOcorrencia": id_ocorrencia,
                            "descricaoOcorrencia": descricaoOcorrencia,
                            "nivelFalha": nivelFalha,
                            "dataTratada": dataTratada,
                            "status": status,
                            "idTeste": data["id"],
                            "maquinaID": data["maquinaID"]["id"],
                            "projetoID": data["projetoID"]["id"],
                            "moduloDescricao": modulo_description,
                            **ocorrencia_flat.as_dict()
                        }
                        all_data.append(ocorrencia_data)

    # Create a DataFrame from the list of dictionaries
    df = pd.json_normalize(all_data)

    # Save the DataFrame to an Excel file
    # todays date in mm-dd-yyyy format 
    today = datetime.today().strftime('%m-%d-%Y')
    output_excel_file = "{today}-gop.xlsx".format(today=today)
    df.to_excel(output_excel_file, index=False)
