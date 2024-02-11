# import random
# import string

# # Define os caracteres possíveis para a senha
# letras_maiusculas = string.ascii_uppercase
# letras_minusculas = string.ascii_lowercase
# numeros = string.digits
# caracteres_especiais = string.punctuation

# # Combina todos os caracteres
# todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

# # Define o tamanho da senha desejada
# tamanho_senha = 12

# # Gera a senha aleatória
# senha_aleatoria = ''.join(random.choice(todos_caracteres) for _ in range(tamanho_senha))

# print(f"Senha aleatória: {senha_aleatoria}")

import random

# Defina os caracteres possíveis para a senha
letras = 'abcdefghijklmnopqrstuvwxyz'
numeros = '0123456789'
caracteres_especiais = '!@#$%^&*()'

# Defina o tamanho da senha desejada
tamanho_senha = 10

# Combine os caracteres
todos_caracteres = letras + numeros + caracteres_especiais

# Gere a senha aleatória
senha_aleatoria = ''.join(random.choice(todos_caracteres) for _ in range(tamanho_senha))

print(f"Senha aleatória: {senha_aleatoria}")
