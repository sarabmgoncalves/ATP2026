import random

menu=((input("Escolha quem iniciará o jogo,(c=Computador/j=Jogador): ")))

if menu != "c" and menu != "j":
    menu=(input("Apenas pode selecionar c ou j,sendo c = computador e j= jogador,para puder escolher quem inicializa o jogo: "))

if menu=="c":
    N=1
    soma=1
    while soma<100:
        N=print(f"O computador selecionou o número {N}, a soma atual é {soma}")
        x = int(input("Insira um número: "))
        if x<0 or x>10:
            x=int(input("Apenas pode introduzir um número entre 1 e 10, tente novamente: "))
        N= 11-x
        soma = soma + N + x
    if soma==100:
        print("O computador ganhou!")

if menu=="j":
    n=0
    soma=0
    while soma<100:
        n=int(input("Introduza um número entre 1 e 10: "))
        if n<0 or n>10:
            n=int(input("Apenas pode introduzir um número entre 1 e 10, tente novamente: "))

        N=random.randint(1,10)
        soma=soma+n+N
        print(f"O computador selecionou o número {N}, a soma atual é {soma}")

        if soma==100:
            print("Computador ganhou!")

        elif soma>100:
            print("Jogador ganhou!")
