def merge_sort(array: list) -> list:
    pass

def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    res = {}
    for item in tuples:
        chave, valore = item[0], item[1]
        if res.get(chave):
            res[chave].append(valore)
        else:
            res[chave] = [valore]
        return res

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))

#{'a': [1, 3], 'b': [2]}