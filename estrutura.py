

"""def busca_sequencial(lista_teste, pesquisado):
    pos = 0
    encontrado = False
    qtd_lista = len(lista_teste)
    
    while pos < qtd_lista and not encontrado:
        if lista_teste[pos] == pesquisado:
            encontrado = True
        else:
            pos +=1

    return encontrado

lista_teste = [1, 2, 32, 8, 17, 256, 25]
print(busca_sequencial(lista_teste, 22))"""


"""def busca_seq_ordenada(lista,pesquisado):
    pos = 0 
    encontrou = False
    parar = False
    qtd_lista = len(lista)

    while pos < qtd_lista and not encontrou and not parar:
        if lista[pos] == pesquisado:
            encontrou = True
        else:
            if lista[pos] > pos:
                parar = True
            else:
                pos += 1

    return encontrou
        

lista = [0, 1, 2, 32, 8, 17, 256, 25]
print(busca_seq_ordenada(lista, 1))"""


"""def busca_binaria(lista, pesquisa):
    inicio = 0
    fim = len(lista)-1
    encontrou = False

    while inicio <= fim and not encontrou:
        meio = (inicio + fim) // 2
        if lista[meio] == pesquisa:
            encontrou = True
        else:
            if pesquisa < lista[meio]:
                fim = meio -1
            else:
                inicio = meio +1

    return encontrou

lista = [0, 1, 2, 8, 13, 17, 19, 32, 42]

print(busca_binaria(lista, 42))"""


"""def busca_binaria(lista, pesquisa):
    if len(lista) == 0:
        return False
    else:
        meio = len(lista) //2
        if lista[meio] == pesquisa:
            return True
        else:
            if lista[meio] > pesquisa:
                return busca_binaria(lista[:meio], pesquisa)
            else:
                return busca_binaria(lista[meio +1:], pesquisa)


lista = [0, 1, 2, 8, 13, 17, 19, 32, 42]

print(busca_binaria(lista, 20))
            """

def busca_binaria(lista,pesquisa):
    inicio = 0
    fim = len(lista)-1
    achei = False
    
    while inicio <= fim and not achei:
        meio = (inicio + fim) // 2
        if lista[meio] == pesquisa:
            achei = True
        else:
            if lista[meio] < pesquisa:
                inicio = meio + 1
            else:
                fim = meio - 1

    return achei
                


