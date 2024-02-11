def pesquisa_binaria(arr, elemento):
    esquerda, direita = 0, len(arr) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if arr[meio] == elemento:
            return meio  # Elemento encontrado
        elif arr[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1  # Elemento não encontrado

# Exemplo de uso
minha_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]
elemento_procurado = 50

resultado = pesquisa_binaria(minha_lista, elemento_procurado)

if resultado != -1:
    print(f"Elemento {elemento_procurado} encontrado na posição {resultado}.")
else:
    print(f"Elemento {elemento_procurado} não encontrado na lista.")
