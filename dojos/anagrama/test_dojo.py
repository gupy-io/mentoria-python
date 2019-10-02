from exercicio.dojo import anagramas

# Aline
# Breno
# Daniel
# Denis
# Diogo
# Heros
# Marina
# Matheus
# Pedro

def teste_uma_letra():
    li = anagramas("b")
    assert li == ["b"]

def teste_uma_letra_2():
    li = anagramas("a")
    assert li == ["a"]

def test_duas_letras():
    li = anagramas("ae")
    assert li == ["ae", "ea"]

def test_duas_letras_2():
    li = anagramas("cb")
    assert li == ["bc", "cb"]

def test_duas_letras_3():
    li = anagramas("aa")
    assert li == ["aa"]

def teste_tres_letras():
    li = anagramas("bff")
    assert li == ["bff", "fbf", "ffb"]

def test_tres_letras_2():
    li = anagramas("aaa")
    assert li == ["aaa"]

def test_tres_letras_3():
    li = anagramas("aab")
    assert li == ["aab", "aba", "baa"]

def test_tres_letras_4():
    li = anagramas("aab")
    assert li == ["aab", "aba", "baa"]

def test_biro():
    li = anagramas("biro")
    assert li == sorted(["biro", "bior", "brio" ,"broi" ,"boir" ,"bori" ,"ibro", "ibor", "irbo", "irob" ,"iobr", "iorb" ,"rbio", "rboi" ,"ribo" ,"riob" ,"roib" ,"robi" ,"obir", "obri" ,"oibr" ,"oirb" ,"orbi", "orib"])