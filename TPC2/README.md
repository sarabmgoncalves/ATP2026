## ATP2026

## Autor

Sara Beatriz Magalhães Gonçalves, a115755

<img width="160" height="120" alt="foto" src="https://github.com/user-attachments/assets/a4529433-778b-4d1d-a630-5cb20b1fc605" />

## Resumo

Foi pedido pelo professor a elaboração de um programa em Python do jogo "Adivinha o número", jogo esse que possui duas modalidades; o computador pensar num número entre 0 e 100 e o utilizador pensar num número entre 0 e 100 .O objetivo principal deste trabalho de casa  é aplicar e consolidar conceitos fundamentais de lógica de programação, com foco especial na estruturação de ciclos de repetição, condições de decisão e manipulação de variáveis ​​de entrada e saída.

## Lista de Resultados
```
import random

print("a) Utilizador adivinha o número.")
print("b) Computador adivinha o número.")
menu= input("Escolha o jogo que deseja jogar:")

if menu == "a":
    numero_secreto = random.randint(0, 100)
    tentativas = 0
    palpite= ""

    while palpite!= numero_secreto:

        palpite = int(input("\nEscolha um número entre 0 e 100: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns, o número era {palpite}! Descobriste o número em {tentativas} tentativa(s).")

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

        print(f"\n O número é {palpite}?")
        resposta = input("Resposta: ")

        if resposta == "O número que pensei é Maior":
            limite_inferior = palpite + 1
        elif resposta == "O número que pensei é Menor":
            limite_superior = palpite - 1

    print(f"O número era {palpite}. Acertei em {tentativas} tentativa(s)!")
```
