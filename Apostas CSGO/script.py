import saldos, time

porcentagem = {
    "Arthur" : [2.50, 1.15],
    "Danilo" : [1.40, 1.50],
    "Gabriel franca" : [1.50, 1.40],
    "Gabriel souza" : [2.50, 1.20],
    "Gustavo" : [1.77, 1.85],
    "Jubao" : [2.10, 1.35],
    "Rubens" : [1.60, 1.45],
    "Paulo" : [1.75, 1.25]
}
lista_escolha = []
lista_jogador = []
lista_apostas = []
lista_nome = []
iniciou = False


while True:
    saldos.saldo()
    oper = int(input("Diga a operação:\n0-Encerra o programa\n1-Iniciar apostas\n2-Finalizar apostas\n"))
    if oper == 0:
        break
    elif oper == 1:
        if not iniciou:
            iniciou = True
            qtd = int(input("Diga quantos participantes jogarão: "))
            for i in range(qtd):
                jogador = input(f"Diga o nome do participante-{i+1}: ").capitalize()
                while jogador not in porcentagem.keys():
                    print("O nome não está na lista de jogadores! Diga um jogador válido.")
                    jogador = input(f"Diga o nome do participante-{i+1}: ").capitalize()
                while jogador in lista_jogador:
                    print("Esse jogador já foi escolhido!")
                    jogador = input(f"Diga o nome do participante-{i+1}: ").capitalize()
                while True:
                    try:
                        aposta = float(input("Diga a sua aposta: "))
                        break
                    except Exception:
                        print("Diga um valor válido!")
                while saldos.apostar(jogador, aposta): # Verifica o saldo do jogador
                    while True:
                        try:
                            aposta = float(input("Você não tem esse dinheiro para apostar!\nDiga uma aposta válida: "))
                            break
                        except Exception:
                            print("Diga um valor válido!")
                nome = input("Em quem você vai apostar: ").capitalize()
                while nome == jogador or nome not in porcentagem.keys():
                    print("Diga um nome válido!")
                    nome = input("Em quem você vai apostar: ").capitalize()
                while True:
                    try:
                        escolha = int(input("1-Over --- 2-Under\n"))
                        break
                    except Exception:
                        print("Diga um valor válido!")
                saldos.retirar(jogador, aposta) # Retira o valor da aposta do saldo
                lista_jogador.append(jogador)
                lista_apostas.append(aposta)
                lista_escolha.append(escolha)
                lista_nome.append(nome)
        else:
            print("Você já iniciou um jogo!")
            time.sleep(1)
    elif oper == 2:
        if iniciou:
            for i, x in enumerate(lista_jogador):
                print(f"Participante - {x}")
                resultado = int(input("0-Perdeu --- 1-Ganhou\n"))
                if resultado == 1:
                    if lista_escolha[i] == 1: # Apostou Over
                        valor = lista_apostas[i] * porcentagem[lista_nome[i]][0]
                        saldos.adicionar(x, valor)
                    else: # Apostou Under
                        valor = lista_apostas[i] * porcentagem[lista_nome[i]][1]
                        saldos.adicionar(x, valor)
                saldos.zerou(x)
            lista_jogador.clear()
            lista_apostas.clear()
            lista_escolha.clear()
            lista_nome.clear()
            iniciou = False
            time.sleep(1)
        else:
            print("Nenhum jogo começou!")
            time.sleep(1)
