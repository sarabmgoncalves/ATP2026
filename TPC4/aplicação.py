import random

def menu():
    print("\n(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")
    op = int(input("\nSelecione uma das opções: "))
    return op

def crialista():
    lista =[]
    tamanho = int(input("Introduza o número de dígitos da lista: "))
    for i in range(tamanho): 
            lista.append(random.randint(1,100))
    return lista

def lerlista():
    lista=[]
    tamanho = int(input("\nIntroduza o número de dígitos da lista: "))
    while len(lista)<tamanho:
            a=int(input("Introduza um número entre 0 e 100: "))
            if 0<= a <= 100:
                lista.append(a)
            else:
                print("\nInválido, deve introduzir um número entre 0 e 100!")
    return lista

def soma(lista):
    return sum(lista)

def media(lista):
    return sum(lista)/len(lista)

def maior_elem(lista):
    i = 0
    res = lista[0]
    while i < len(lista): 
        if lista[i] > res:
            res = lista[i]
        i = i + 1
    return res

def menor_elem(lista):
    i = 0
    res = lista[0]
    while i < len(lista): 
        if lista[i] < res:
            res = lista[i]
        i = i + 1
    return res

def listaordenada_c(lista):
    i=0
    res="Sim"
    while i<len(lista)-1:
        if lista[i]>lista[i+1]:
            res= "Não"
        i=i+1
    return res

def listaordenada_d(lista):
    i = 0
    res = "Sim"
    while i < len(lista) - 1:
        if lista[i] < lista[i + 1]:
            res= "Não"
        i = i + 1
    return res

def posicao(lista):
    res=-1
    elem = int(input("Insira o elemento que deseja procurar e localizar o seu indice na lista: "))
    i=0
    while i<len(lista):
        if lista[i]==elem:
            res= i
        i=i+1
    return res

def main():
    op = menu()
    lista = []
    res = 0
    while op != 0:
        if op == 1:
            lista = crialista()
            print(lista)
        elif op == 2:
            lista = lerlista()
            print(lista)
        elif len(lista) == 0:
            print("Precisa de criar uma lista, escolha a opção 1 ou 2 primeiro!")
        elif op == 3:
            print("Soma dos valores da lista: ",soma(lista))
        elif op == 4:
            print("Média dos valores da lista: ",media(lista))
        elif op==5:
            print("O maior elemento da lista: ",maior_elem(lista))
        elif op==6:
            print("O menor elemento da lista: ",menor_elem(lista))
        elif op==7:
            print("A lista está ordenada por ordem crecente: ",listaordenada_c(lista))
        elif op==8:
            print("A lista está ordenada por ordem decrescente: ",listaordenada_d(lista))
        elif op==9:
            print("O elemento escolhido encontra-se na posição: ",posicao(lista))
        else:
            print("\nOpção não implementada. Selecione outra opção!")
        op = menu()

    if len(lista) == 0:
        print("Não foi criada nenhuma lista!")
    else:
        print(f"Lista armazenada {lista}")
    return lista, res

lista, res = main()