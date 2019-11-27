from typing import List
import importlib
import inspect
import sys
import os
import re
from pathlib import Path
from pprint import pprint


class Testador:
    sucesso: int = 0
    falhas: int = 0

    def coletor_de_testes(self, pasta: str = './testes'):
        testes: List = []
        for arquivo in Path(pasta).glob("teste_*.py"):
            modulo_de_testes = importlib.import_module(
                re.sub(".py", "", re.sub(os.sep, ".", str(arquivo)))
            )
            testes_encontrados = [
                teste
                for nome, teste in inspect.getmembers(modulo_de_testes)
                if nome.startswith("teste_") and callable(teste)
            ]
            lista_nome_dos_testes = [teste.__name__ for teste in testes_encontrados]
            testes.append((arquivo, testes_encontrados))
        return testes, lista_nome_dos_testes

    def executador_de_teste(self, pasta: str = './testes'):
        resultados: List = []
        testes_encontrados, _ = self.coletor_de_testes(pasta)
        for modulo, testes in testes_encontrados:
            for teste in testes:
                resultado_do_teste = {"modulo": modulo, "nome": teste.__name__}
                try:
                    teste()
                except AssertionError:
                    resultado_do_teste["estado"] = "falhou"
                    self.falhas += 1
                else:
                    resultado_do_teste["estado"] = "passou"
                    self.sucesso += 1
                resultados.append(resultado_do_teste)
        return resultados

    def run(self, pasta: str = "./testes"):
        for res in self.executador_de_teste(pasta):
            pprint(f"> {res['modulo']}:{res['nome']} - {res['estado']}")
            pprint(f"{'---'*20}")

        pprint(f"numero de testes coletados {self.falhas + self.sucesso}")

        if self.falhas > 0:
            pprint("MAAA OLHA O ERRO AI, VAMOS ARRUMAR ESSE TESTINHO")
            sys.exit(1)


if __name__ == "__main__":
    teste = Testador()
    # teste.coletor_de_testes()
    # teste.executador_de_teste()
    teste.run()
