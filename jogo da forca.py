def desenho(erros):
    if erros == 0:
        print("|-----")
        print("|    |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_")
    elif erros == 1:
        print("|-----")
        print("|    |")
        print("|    O")
        print("|")
        print("|")
        print("|")
        print("_")
    # Adicione os outros desenhos para os erros restantes

def jogo_da_forca():
    palavra_secreta = "PYTHON"  # Defina a palavra secreta aqui
    senha_list = [letra for letra in palavra_secreta]
    chances = 6
    tentativas = []

    while chances > 0:
        print("A palavra:", " ".join(senha_list))
        letra = input("Digite uma letra: ").upper()

        if letra in tentativas:
            print("Você já tentou essa letra!")
        elif letra in senha_list:
            print("Você acertou uma letra!")
            tentativas.append(letra)
        else:
            print("Não há essa letra na palavra!")
            tentativas.append(letra)
            chances -= 1
            desenho(6 - chances)

        if set(senha_list) == set(tentativas):
            print("Parabéns, você acertou a palavra!")
            break

    if chances == 0:
        print("Você perdeu! A palavra era:", palavra_secreta)

jogo_da_forca()
