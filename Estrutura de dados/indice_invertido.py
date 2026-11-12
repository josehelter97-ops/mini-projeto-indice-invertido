import re

def construir_indice(texto): # Usado para identificar palavras e ignorar pontuações 
    indice = {} #Criei o dicionário

    linhas = texto.splitlines() # Separa o texto em linhas

    for numero_linha, linha in enumerate(linhas, start=1):
        palavras = re.findall(r'\w+', linha.lower())

        for palavra in set(palavras): # usei para não processar a mesma palavra
            if palavra not in indice:
                indice [palavra] = set()

            indice[palavra].add(numero_linha) # Coloca o numero da linha no conjunto
    
    return indice    

def buscar(indice,palavra): # Essa função procura a palavra no indice invertido e informa as linhas
    palavra = palavra.lower()

    linhas = indice.get(palavra,set()) # Procura uma chave no dicionário

    return sorted(linhas) # Transforma o conjunto em lista ordenada


def buscar_e(indice, palavras): # Criando interseção
    if not palavras: 
        return [] # Verifica se a lista está vazia

    resultado = set(indice.get(palavras[0].lower(), set()))

    for palavra in palavras[1:]:
        resultado = resultado & indice.get(palavra.lower(), set())

    return sorted(resultado)

def buscar_ou(indice, palavras): # Retorna a linha que tem pelo menos uma palavra
    resultado = set()

    for palavra in palavras:
        resultado = resultado | indice.get(palavra.lower(), set())

    return sorted(resultado)