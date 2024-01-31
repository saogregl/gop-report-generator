# Create a function that returns the query string based on a given map of parameters.
# Example:


def query(dict):
    return "&".join(["{}={}".format(k, v) for k, v in dict.items()])

def query_gop(idProjeto, idMaquina, idTeste):

    dict_query = {
        "ocorrencia.teste.maquina.projeto.id": idProjeto,
        "ocorrencia.teste.maquina.id": idMaquina,
        "ocorrencia.teste.id": idTeste,
        "ocorrencia.id": "",
        "ocorrencia.status[0].status.id": "",
        "ocorrencia.modulosOcorrencia[0].descricao": "",
        "ocorrencia.componentesOcorrencia[0].descricao": "",
        "ocorrencia.nivelFalha.id": "",
        "ocorrencia.origem.id": "",
        "ocorrencia.responsavel.perfilPessoa.id": "",
        "ocorrencia.responsavel.id": "",
        "ocorrencia.tipoOcorrencia.id": "",
        "ocorrencia.inspetor.id": "",
        "dataInicial": "",
        "dataFinal": "",
    }

    return query(dict_query)

print("The query string is: ")
print(query_gop(1441, 2154, 1))