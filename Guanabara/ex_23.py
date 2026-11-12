
lista = [1, 2, 3, 4, 5]


def inverter(lista):
    p = PilhaArray()
    i = 0
    while i < len(lista):
        p.push(lista[i])
        i += 1
        print(lista)
    i = 0
    while not p.is_empty():
        lista[i] = p.pop()
        i += 1
    return lista

print(inverter(lista))