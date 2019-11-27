from unittest import TestCase, main
from testa_v1 import testa_v1_coletador, executa_teste
from pathlib import PosixPath

class TestaNossoTestador(TestCase):
    def test_nosso_coletor(self):
        testes_esperados = ['teste_funcao_de_soma', 'teste_numero']
        _, lista_de_testes = testa_v1_coletador('./testes')
        self.assertEqual(testes_esperados, lista_de_testes)

    def testa_nosso_executor_dos_testes(self):
        resultados_do_executor = [{'estado': 'falhou', 'modulo': PosixPath('testes/teste_code.py'), 'nome': 'teste_funcao_de_soma'}, {'estado': 'passou', 'modulo': PosixPath('testes/teste_code.py'), 'nome': 'teste_numero'}]
        saida_do_executor = executa_teste('./testes')
        self.assertEqual(resultados_do_executor, saida_do_executor)

    def teste_saida_do_testador(self):
        pass

if __name__ == '__main__':
    main()
