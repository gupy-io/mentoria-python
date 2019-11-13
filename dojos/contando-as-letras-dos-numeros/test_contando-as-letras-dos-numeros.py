# Aline Breno Diogo  Leandro Matheus  Pedro Rafael
"""
Este problema foi utilizado em 186 Dojo(s).

Se os números de 1 a 5 fossem escritos em palavras: 
um, dois, três, quatro, cinco, então teríamos 
utilizado 2 + 4 + 4 + 6 + 5 = 21 letras no total.

Se todos os números de 1 até 1000 fossem escritos
em palavras, quantas letras nós teríamos utilizado?
"""

"""
Onde paramos, estavamos criando uma função para converter uma lista de numeros para um lista de numeros por extenso

O que podemos melhorar?
Nomes de variaveis?
Nomes de funções?
Respeitar o padrão de entrada da função?

Caso você tenha alguma sugestão só abrir um PR
"""
def contar_letras(palavras):
    if isinstance(palavras, list):
        return len(''.join(palavras))
    lista_de_palavras = palavras.split(', ')
    lista_junta = ''.join(lista_de_palavras)
    return len(lista_junta)

def converte_lista_de_numero_em_string(lista):
    result = []
    for i in lista:
        result.append(converte_numero_em_palavra(i))
    return result

def converte_numero_em_palavra(numero):
    lista = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze']
    if numero < 13:
        return lista[numero-1]

def test_contar_uma_palavra():
    assert contar_letras("um") == 2

def test_soma_contagem_de_letras():
    assert contar_letras(['um', 'dois']) == 6

def test_soma_tres_palavras():
    assert contar_letras("um, dois, tres") == 10

def test_converter_em_string():
    lista_1_a_12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert converte_lista_de_numero_em_string(lista_1_a_12) == ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze']



