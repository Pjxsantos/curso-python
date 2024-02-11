# texto = "Este é um exemplo de texto para contar palavras em Python"
# palavras = texto.split()  # Divide o texto em palavras

# numero_palavras = len(palavras)  # Conta o número de palavras

# print(f"O texto tem {numero_palavras} palavras.")

# Exemplo 2

# from collections import Counter

# texto = "Este é um exemplo de texto para contar palavras em Python"
# palavras_contagem = Counter(texto.split())

# for palavra, quantidade in palavras_contagem.items():
#     print(f"{palavra}: {quantidade}")

#Exemplo 3

from collections import Counter

texto = "Este é um exemplo de texto para contar palavras em Python"
palavras_contagem = Counter(texto.split())

for palavra, quantidade in palavras_contagem.items():
    print(f"{palavra}: {quantidade}")


