from indice_invertido import (
    construir_indice,
    buscar,
    buscar_e,
    buscar_ou
)

def main():
    print("----Caça palavras em textos----")
    print("Digite o que você deseja procurar")
    print("Digite FIM para terminar")

    linhas = []

    while True:
        linha = input

        if linha.upper == "FIM:"
            break

        linhas.append(linha)

    texto = "\n".join(linhas)

    indice = construir_indice(texto)

    print("\nPesquisa realizada com sucesso")


    while True:
        print("\nEscolha uma opção:")
        print("1 - Buscar uma palavra")
        print("2 - Buscar com E")
        print("3 - Buscar com OU")
        print("0 - Sair")

        opcao = input("\nDigite sua opção: ")

        if opcao == "0":
            print("Encerrando o programa...")
            break

        elif opcao == "1":
            palavra = input("Digite a palavra: ")

            resultado = buscar(indice, palavra)

            print("Linhas encontradas:", resultado)

        elif opcao == "2":
            palavras = input(
                "Digite as palavras separadas por vírgula: "
            ).split(",")

            palavras = [p.strip() for p in palavras]

            resultado = buscar_e(indice, palavras)

            print("Linhas encontradas:", resultado)

        elif opcao == "3":
            palavras = input(
                "Digite as palavras separadas por vírgula: "
            ).split(",")

            palavras = [p.strip() for p in palavras]

            resultado = buscar_ou(indice, palavras)

            print("Linhas encontradas:", resultado)

        else:
            print("Opção inválida. Tente novamente.")

