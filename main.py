import random

tabla = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

print("Salut! Bun venit la x si 0")
jucator = input("Cu ce doresti sa joci ? x sau 0?")
if (jucator == 'x'):
    calculator = '0'
else:
    calculator = 'x'

def AfiseazaTabla(tabla):
    print(tabla[1] + "|" + tabla[2] + "|" + tabla[3])
    print("-+-+-")
    print(tabla[4] + "|" + tabla[5] + "|" + tabla[6])
    print("-+-+-")
    print(tabla[7] + "|" + tabla[8] + "|" + tabla[9])
    print("\n")


def EsteCampLiber(pozitie):
    if tabla[pozitie] == ' ':
        return True
    else:
        return False


def InsereazaLitera(litera, pozitie):
    if EsteCampLiber(pozitie):
        tabla[pozitie] = litera
        AfiseazaTabla(tabla)
        if Egalitate():
            print("Egalitate")
            exit()
        if AiCastigat():
            if litera == calculator:
                print("Calculatorul a castigat")
                exit()
            else:
                print("Ai castigat")
                exit()
            return
    else:
        print("Casuta deja completata! Incercati sa completati o casuta goala")
        pozitie = int(input("Reintroduceti litera: "))
        InsereazaLitera(litera, pozitie)
        return


def Egalitate():
    for i in tabla.keys():
        if (tabla[i] == ' '):
            return False
    return True


def AiCastigat():
    if tabla[1] == tabla[2] and tabla[1] == tabla[3] and tabla[1] != ' ':
        return True
    elif tabla[4] == tabla[5] and tabla[4] == tabla[6] and tabla[4] != ' ':
        return True
    elif tabla[7] == tabla[8] and tabla[7] == tabla[9] and tabla[7] != ' ':
        return True
    elif tabla[1] == tabla[4] and tabla[1] == tabla[7] and tabla[1] != ' ':
        return True
    elif tabla[2] == tabla[5] and tabla[2] == tabla[8] and tabla[2] != ' ':
        return True
    elif tabla[3] == tabla[6] and tabla[3] == tabla[9] and tabla[3] != ' ':
        return True
    elif tabla[1] == tabla[5] and tabla[1] == tabla[9] and tabla[1] != ' ':
        return True
    elif tabla[3] == tabla[5] and tabla[3] == tabla[7] and tabla[3] != ' ':
        return True
    else:
        return False


def VerificaLaturaCastigatoare(mark):
    if tabla[1] == tabla[2] and tabla[1] == tabla[3] and tabla[1] == mark:
        return True
    elif tabla[4] == tabla[5] and tabla[4] == tabla[6] and tabla[4] == mark:
        return True
    elif tabla[7] == tabla[8] and tabla[7] == tabla[9] and tabla[7] == mark:
        return True
    elif tabla[1] == tabla[4] and tabla[1] == tabla[7] and tabla[1] == mark:
        return True
    elif tabla[2] == tabla[5] and tabla[2] == tabla[8] and tabla[2] == mark:
        return True
    elif tabla[3] == tabla[6] and tabla[3] == tabla[9] and tabla[3] == mark:
        return True
    elif tabla[1] == tabla[5] and tabla[1] == tabla[9] and tabla[1] == mark:
        return True
    elif tabla[3] == tabla[5] and tabla[3] == tabla[7] and tabla[3] == mark:
        return True
    else:
        return False


def MiscareJucator():
    pozitie = int(input("Introdu pozitia pentru "+ jucator+": "))
    if(pozitie<1 or pozitie > 9):
        print("Tabla de joc contine 9 patratele de completat,cuprinse intre 1 si 9 inclusiv \n")
        MiscareJucator()
        return
    InsereazaLitera(jucator, pozitie)
    return


def MiscareCalculator():
    CelMaiMareScor = -1000
    CeaMaiBunaMiscare = 0

    for i in tabla.keys():
        if tabla[i] == ' ':
            tabla[i] = calculator
            scor = MinMax(tabla, False)
            tabla[i] = ' '
            if (scor > CelMaiMareScor):
                CelMaiMareScor = scor
                CeaMaiBunaMiscare = i
    InsereazaLitera(calculator, CeaMaiBunaMiscare)
    return


def MinMax(tabla, Maximizare):
    if VerificaLaturaCastigatoare(calculator):
        return 100
    elif VerificaLaturaCastigatoare(jucator):
        return -100
    elif Egalitate():
        return 0
    if Maximizare:
        CelMaiMareScor = -1000

        for i in tabla.keys():
            if tabla[i] == ' ':
                tabla[i] = calculator
                scor = MinMax(tabla, False)
                tabla[i] = ' '
                if (scor > CelMaiMareScor):
                    CelMaiMareScor = scor
        return CelMaiMareScor
    else:
        CelMaiMareScor = 800

        for i in tabla.keys():
            if tabla[i] == ' ':
                tabla[i] = jucator
                scor = MinMax(tabla, True)
                tabla[i] = ' '
                if scor < CelMaiMareScor:
                    CelMaiMareScor = scor
        return CelMaiMareScor


def TragereLaSort():
    primul = random.randint(1, 2)
    if (primul == 1):
        return True
    else:
        return False

AfiseazaTabla(tabla)

if (TragereLaSort()):
    print("Prin tragere la sort ai fost ales sa faci prima mutare! Succes")
    while not AiCastigat():
        MiscareJucator()
        MiscareCalculator()
else:
    print("Prin tragere la sort ,calculatorul va face prima mutare! Succes")
    while not AiCastigat():
        MiscareCalculator()
        MiscareJucator()
