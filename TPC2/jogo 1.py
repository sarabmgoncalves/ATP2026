import random

print("a) Utilizador adivinha o número.")
print("b) Computador adivinha o número.")
menu= input("Escolha o jogo que deseja jogar:")

if menu == "a":
    numero_secreto = random.randint(0, 100)
    tentativas = 0

    while True:
        palpite = int(input("\n Escolha um número entre 0 e 100: ")) 
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns, o número era {palpite}! Descobriste o número em {tentativas} tentativa(s).")
            break
        elif palpite < numero_secreto:
            print("O número que pensei é Maior")
        else:
            print("O número que pensei é Menor")

if menu== "b":
    limite_inferior=0
    limite_superior=100
    tentativas = 0

    resposta = ""

    while resposta != "Acertas-te":
        palpite = (limite_inferior + limite_superior) // 2
        tentativas = tentativas + 1

        print(f"\nO número é {palpite}?")
        resposta = input("Resposta: ")

        if resposta == "O número que selecionei é Maior":
            limite_inferior = palpite + 1
        elif resposta == "O número que selecionei é Menor":
            limite_superior = palpite - 1

    print(f"O número era {palpite}. Acertei em {tentativas} tentativa(s)!")