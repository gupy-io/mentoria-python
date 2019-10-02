from itertools import permutations

def anagramas(text):
        li = []
        for sub in permutations(text, len(text)):
            li.append(''.join(list(sub)))
        return sorted(list(set(li)))
