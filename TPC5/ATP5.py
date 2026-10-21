def menu():
    print(""" 
    1: Criar uma turma;
    2: Inserir um aluno na turma;
    3: Listar a turma;
    4: Consultar um aluno por id;
    5: Guardar a turma dum ficheiro;
    6: Carregar uma turma dum ficheiro;
    0: Sair da aplicação; 
    """)
    op=int(input("Selecione a operação desejada: "))
    while op<0 or op>6:
        print(" Selecione uma opção válida!")
        op=int(input(" Selecione a operação desejada: "))

    return op

def criarturma():
    t = int(input("\nQuantos elementos terá a turma? Tem que ter no mínimo 5 elementos! "))
    turma = []
    n=0

    while t<5:
        print("A turma deve ter no mínimo 5 elementos!")
        t = int(input("\nQuantos elementos terá a turma? Tem que ter no mínimo 5 elementos! "))

    while n<t:
        nome=input("\nNome: ")
        id=int(input("Id do aluno: "))
        aluno = (nome, id, notas())
        turma.append(aluno)
        n=n+1

    return turma


def inseriraluno(turma):
    al=int(input("Quantos alunos deseja inserir na turma? "))
    n=0

    while al > n:
        nome=input("\nNome: ")
        id=int(input("Id do aluno: "))
        aluno_ins = (nome, id,notas())
        turma.insert(0, aluno_ins)
        n=n+1
    return turma

def consultaid(turma):
    id=int(input("Insira o id do aluno: "))
    n=0
    encontrei=False

    while n < len(turma):
        aluno=turma[n]
        if aluno[1]==id:
            print("Nome: ", aluno[0])
            print("Id: ", aluno[1])
            print("Nota do tpc: ",aluno[2][0])
            print("Nota do projeto: ",aluno[2][1])
            print("Nota do teste: ",aluno[2][2])
            encontrei=True
        n=n+1

    if not encontrei:
        print("Aluno não encontrado!")

def ficheiro(turma):
    f1 = open("turma_atp5.txt","w")
    
    for aluno in turma:
        f1.write( (aluno[0]) + "|"+  str(aluno[1]) + "|" + str(aluno[2][0]) + "|" + str(aluno[2][1]) + "|"
                +  str(aluno[2][2]) + "\n")
    f1.close()
    return

def carregar():
    turma = []
    f1 = open("turma_atp5.txt", "r")

    for linha in f1:
        linha = linha.strip()
        if linha != "":
            campos = linha.split("|")
            aluno = ( campos[0],int(campos[1]),[float(campos[2]),float(campos[3]),float(campos[4])])
            turma.append(aluno)

    f1.close()
    return turma

def notas():
        tpc = float(input("Nota do tpc: "))
        while tpc<0 or tpc>20:
            print("A escala é de 0 a 20! Valores abaixo de 0 ou acima de 20 não são válidos, tente novamente!")
            tpc = float(input("Nota do tpc: "))
        
        proj = float(input("Nota do projeto: "))
        while proj<0 or proj>20:
            print("A escala é de 0 a 20! Valores abaixo de 0 ou acima de 20 não são válidos, tente novamente!")
            proj = float(input("Nota do projeto: "))
        
        teste = float(input("Nota do teste: "))
        while teste<0 or teste>20:
            print("A escala é de 0 a 20! Valores abaixo de 0 ou acima de 20 não são válidos, tente novamente!")
            teste = float(input("Nota do teste: "))
            
        return [tpc,proj,teste]
     

turma = []
op = -1

while op != 0: 

    op = menu()

    if op == 1:
        turma = criarturma()

    elif op == 2:
        turma = inseriraluno(turma)

    elif op == 3:
        for aluno in turma:
            print("Nome:", aluno[0], "| Id:", aluno[1],
                  "| Nota do tpc:", aluno[2][0],
                  "| Nota do projeto:", aluno[2][1],
                  "| Nota do teste:", aluno[2][2])
    elif op == 4:
        consultaid(turma)

    elif op==5:
        ficheiro(turma)

    elif op==6:
        turma=carregar()
        
    elif op==0:
        print("Aplicação foi encerrada!")
        exit()
        