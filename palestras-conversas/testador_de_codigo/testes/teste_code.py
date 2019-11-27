def soma(a: int, b: int) -> int:
    return a + b


def teste_numero():
    assert 1 == 1


def teste_funcao_de_soma():
    assert 2 == 2


def teste_soma():
    assert 2 == soma(1, 1)


def teste_soma_maior():
    assert 3 > soma(1, 1)
