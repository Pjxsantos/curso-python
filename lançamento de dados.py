import random

def gera_dado():
    # Gera um número aleatório entre 1 e 6 (representando as faces do dado)
    return random.randint(1, 6)

def main():
    num_lancamentos = int(input("Quantos lançamentos de dado você deseja simular? "))

    resultados = [gera_dado() for _ in range(num_lancamentos)]

    print(f"Resultados dos {num_lancamentos} lançamentos:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"Lançamento {i}: {resultado}")

if __name__ == "__main__":
    main()
