import importlib
import inspect
import sys
import os
import re
from collections import defaultdict
from pathlib import Path
from pprint import pprint


def testa_v1_coletador(pasta):
    testes = []
    lista_nome_dos_testes = []
    for arquivo_de_teste in Path(pasta).glob("teste_*.py"):
        modulo_de_testes = importlib.import_module(
            re.sub(".py", "", re.sub(os.sep, "." , str(arquivo_de_teste)))
        )
        testes_encontrados =[
            teste
            for nome, teste in inspect.getmembers(modulo_de_testes)
            if nome.startswith("teste_") and callable(teste)
        ]
        lista_nome_dos_testes = [teste.__name__ for teste in testes_encontrados]
        testes.append((arquivo_de_teste, testes_encontrados))
    return testes, lista_nome_dos_testes


def executa_teste(pasta):
    resultados = []

    testes_encontrados, _ = testa_v1_coletador(pasta)
    for modulo, testes in testes_encontrados:
        for teste in testes:
            resultado_de_um_teste = {"modulo": modulo, "nome": teste.__name__}
            try:
                teste()
            except AssertionError:
                resultado_de_um_teste["estado"] =  "falhou"
            else:
                resultado_de_um_teste["estado"] = "passou"
            resultados.append(resultado_de_um_teste)
    return resultados


def rodar_os_teste(pasta="./testes"):
    falhas: int = 0
    sucesso: int = 0
    for res in executa_teste(pasta):
        pprint(f"> {res['modulo']}:{res['nome']} - {res['estado']}")
        pprint(f"{'---'*20}")

        if res["estado"] == 'falhou':
            falhas += 1

        if res["estado"] == "passou" :
            sucesso += 1

    pprint(f"numero de testes coletados {falhas + sucesso}")

    if falhas > 0:
        pprint(f"ERROOOOOOOUUU ARRUMA ESSE TESTE AI IRMAO")
        sys.exit(1)

if __name__ == "__main__":
    rodar_os_teste()
