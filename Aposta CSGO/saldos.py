import shutil, tempfile

def saldo():
    for i in range(3):
        print()
    for i in open('saldos.txt', 'r'):
        print(f"Saldo de {i}", end="")
    for i in range(2):
        print()
def apostar(nome, aposta):
    with open('saldos.txt', 'r') as arquivo, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
        for linha in arquivo:
            if nome in linha[:18]:
                codigo = float(linha[18:21])
                if aposta > codigo:
                    return True
    return False
def retirar(nome, aposta):
    with open('saldos.txt', 'r') as arquivo, \
            tempfile.NamedTemporaryFile('w', delete=False) as out:
            for linha in arquivo:
                if nome in linha[:18]:
                    codigo = float(linha[18:21])
                    codigo -= aposta
                    linha = linha[:18] + str(f"{codigo:.2f}") + " coins\n"
                out.write(linha)
    shutil.move(out.name, 'saldos.txt')
def adicionar(nome, valor):
    with open('saldos.txt', 'r') as arquivo, \
            tempfile.NamedTemporaryFile('w', delete=False) as out:
            for linha in arquivo:
                if nome in linha[:18]:
                    codigo = float(linha[18:21])
                    codigo += valor
                    linha = linha[:18] + str(f"{codigo:.2f}") + " coins\n"
                out.write(linha)
    shutil.move(out.name, 'saldos.txt')