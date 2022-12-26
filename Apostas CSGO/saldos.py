import shutil, tempfile

def saldo():
    for i in range(3):
        print()
    for i in open('Apostas CSGO\saldos.txt', 'r'):
        print(f"Saldo de {i}", end="")
    for i in range(2):
        print()

def apostar(nome, aposta):
    with open('Apostas CSGO\saldos.txt', 'r') as arquivo, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
        for linha in arquivo:
            if nome in linha[:18]:
                codigo = float(linha[18:22])
                if aposta > codigo:
                    return True
    return False

def retirar(nome, aposta):
    with open('Apostas CSGO\saldos.txt', 'r') as arquivo, \
            tempfile.NamedTemporaryFile('w', delete=False) as out:
            for linha in arquivo:
                if nome in linha[:18]:
                    codigo = float(linha[18:22])
                    codigo -= aposta
                    linha = linha[:18] + str(f"{codigo:.2f}") + " coins\n"
                out.write(linha)
    shutil.move(out.name, 'Apostas CSGO\saldos.txt')
    
def adicionar(nome, valor):
    with open('Apostas CSGO\saldos.txt', 'r') as arquivo, \
            tempfile.NamedTemporaryFile('w', delete=False) as out:
            for linha in arquivo:
                if nome in linha[:18]:
                    codigo = float(linha[18:22])
                    codigo += valor
                    linha = linha[:18] + str(f"{codigo:.2f}") + " coins\n"
                out.write(linha)
    shutil.move(out.name, 'Apostas CSGO\saldos.txt')

def zerou(nome):
    with open('Apostas CSGO\saldos.txt', 'r') as arquivo, \
            tempfile.NamedTemporaryFile('w', delete=False) as out:
            for linha in arquivo:
                if nome in linha[:18]:
                    codigo = float(linha[18:22])
                    if codigo == 0:
                        linha = linha[:18] + str(00.25) + " coins\n"
                        print(f"O jogador {nome} zerou o saldo, logo fica com 0.25 coins.")
                    else:
                        print(f"O jogador {nome} não zerou.")
                out.write(linha)
    shutil.move(out.name, 'Apostas CSGO\saldos.txt')