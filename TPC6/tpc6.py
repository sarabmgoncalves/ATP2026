def menu(lista):
    for op in lista:
        print(op)

menuOpcoes = ["""
(1) Carregar tabela meteorológica de um ficheiro
(2) Gravar tabela meteorológica num ficheiro 
(3) Temperatura média de cada dia
(4) Temperatura mínima mais baixa registada 
(5) Calcular a amplitude térmica de cada dia
(6) Valor máximo de precipitação registada
(7) Dias de precipitação superior ao limite definido
(8) Maior número consecutivo de dias com precipitação abaixo do limite definido
(0) Sair\n"""]

tabMeteo1 = [((2022,1,20), 2, 16, 0), ((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

def carregaTabMeteo(fnome):
    res = []
    f = open(fnome, "r")
    for linha in f:
        campos = linha.strip().split(',')
        novadata = campos[0].split('|')
        res.append(((int(novadata[0]), int(novadata[1]), int(novadata[2])),
                    float(campos[1]), float(campos[2]), float(campos[3])))
    f.close()
    return res

def guardaTabMeteo(t, fnome):
    f = open(fnome, "w")
    for registo in t:
        f.write(f"{registo[0][0]}|{registo[0][1]}|{registo[0][2]},{registo[1]},{registo[2]},{registo[3]}\n")
    f.close()

def medias(tabMeteo1):
    res = []
    for data, tmin, tmax, _ in tabMeteo1:
        res.append((data, (tmax + tmin) / 2))
    return res

def minMin(tabMeteo1):
    minima = tabMeteo1[0][1]
    for _, tmin, _, _ in tabMeteo1:
        if tmin < minima:
            minima = tmin
    return minima

def amplTerm(tabMeteo1):
    res = []
    for data, tmin, tmax, _ in tabMeteo1:
        res.append((data, tmax - tmin))
    return res

def maxChuva(tabMeteo1):
    max_prec=tabMeteo1 [0][1]
    for max_data,_,_,prec in tabMeteo1:
        if max_prec<prec:
            max_prec=prec

    return (max_data, max_prec)

def diasChuvosos(tabMeteo1, pmin):
    res = []
    for data, _, _, prec in tabMeteo1:
        if prec > pmin:
            res.append((data, prec))
    return res

def maxPeriodoCalor(tabMeteo, p):
    maximo=0
    atual=0
    for _, _, _,prec in tabMeteo:
        if prec < p:
            atual += 1
        if prec>p:
            maximo=atual
    return maximo

menu(menuOpcoes)
op = input("Qual a opção pretendida? ")

while op != '0':
    if op == '1':
        ficheiro = input("Introduza o nome do ficheiro a ler: ")
        tabMeteo1 = carregaTabMeteo(ficheiro)
        print(tabMeteo1)
    elif op == '2':
        guardaTabMeteo(tabMeteo1, "meteorologia.txt")
    elif op == '3':
        print(medias(tabMeteo1))
    elif op == '4':
        print(minMin(tabMeteo1))
    elif op == '5':
        print(amplTerm(tabMeteo1))
    elif op=='6':
        print(maxChuva(tabMeteo1))
    elif op == '7':
        pmin = float(input("Defina um valor de precipitação: "))
        print(diasChuvosos(tabMeteo1, pmin))
    elif op == '8':
        p = float(input("Defina um valor de precipitação: "))
        print(maxPeriodoCalor(tabMeteo1, p))
    elif op=='0':
            pass
    else:
        print("Operação desconhecida!")
    menu(menuOpcoes)
    op = input("Qual a opção pretendida? ")