import saldos

porcentagem = {
    "Arthur" : [1.8, 1.7],
    "Danilo" : [1.5, 1.8],
    "Gabriel frança" : [1.4, 1.6],
    "Gabriel souza" : [1.3, 1.6],
    "Gustavo" : [1.77, 1.85],
    "Jubão" : [1.5, 1.4],
    "Rubens" : [1.8, 1.5]
}
lista_escolha = []
lista_jogador = []
lista_apostas = []
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
                    except ValueError:
                        print("Diga um valor válido!")
                while saldos.apostar(jogador, aposta):
                    while True:
                        try:
                            aposta = float(input("Você não tem esse dinheiro para apostar!\nDiga uma aposta válida: "))
                            break
                        except ValueError:
                            print("Diga um valor válido!")
                nome = input("Em quem você vai apostar: ").capitalize()
                while nome == jogador or nome not in porcentagem.keys():
                    print("Diga um nome válido!")
                    nome = input("Em quem você vai apostar: ").capitalize()
                while True:
                    try:
                        escolha = int(input("1-Over --- 2-Under\n"))
                        break
                    except ValueError:
                        print("Diga um valor válido!")
                saldos.retirar(jogador, aposta)
                lista_jogador.append(jogador)
                lista_apostas.append(aposta)
                lista_escolha.append(escolha)
        else:
            print("Você já iniciou um jogo!")
    elif oper == 2:
        if iniciou:
            for i, x in enumerate(lista_jogador):
                print(f"Participante - {x}")
                resultado = int(input("0-Perdeu --- 1-Ganhou\n"))
                if resultado == 1:
                    if lista_escolha[i] == 1:
                        valor = lista_apostas[i] * porcentagem[x][0]
                        saldos.adicionar(x, valor)
                    else:
                        valor = lista_apostas[i] * porcentagem[x][1]
                        saldos.adicionar(x, valor)
            lista_jogador = []
            lista_apostas = []
            lista_escolha = []
            iniciou = False
        else:
            print("Nenhum jogo começou!")