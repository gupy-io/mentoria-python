# Breno, Daniel, Diogo, Matheus, Rafa, Breno

def test_um_retorna_feliz():
    assert calcula_feliz(1) == 'Feliz'

def test_sete_retorna_feliz():
    assert calcula_feliz(7) == 'Feliz'

def test_zero_retorna_triste():
    assert calcula_feliz(0) == 'Tixti'

# ESSE CASO ESTA EM LOOP INFINITO
def test_2_retorna_():
    assert calcula_feliz(2) == 'Tixti'


def calcula_feliz(numero):
    novo_numero = 0
    for digito in str(numero):
        novo_numero += int(digito)**2
    if novo_numero == 1:
        return 'Feliz'
    # TODO: não foi descoberto quais os numeros não feliz..
    # O QUE ACONTECEU O NUMERO REPETIU VARIAS VEZES UMA SEQUENCIA e não conseguimos
    # descobrir qual o criteiro de parada ou seja quando o numero é tixti
    elif novo_numero == 0:
        return 'Tixti'
    else:
        return calcula_feliz(novo_numero)

