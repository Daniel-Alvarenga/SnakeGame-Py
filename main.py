from colorama import Fore, Style, init
import random
import os
import time
import keyboard

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def nova_maca(cobra, tamanho):
    x_maca = random.randint(0, tamanho - 1)
    y_maca = random.randint(0, tamanho - 1)

    if not [x_maca, y_maca] in cobra:
        return [x_maca, y_maca]
    else:
        return nova_maca(cobra, tamanho)
    
def nova_protecao(cobra, tamanho, maca):
    x_protecao = random.randint(0, tamanho - 1)
    y_protecao = random.randint(0, tamanho - 1)

    if not [x_protecao, y_protecao] in cobra and not [x_protecao, y_protecao] == maca:
        return [x_protecao, y_protecao]
    else:
        return nova_protecao(cobra, tamanho, maca)

direcao = "d"

def pressionar_tecla(event):
    if event.event_type == keyboard.KEY_DOWN:
        global direcao
        global direcao_executada

        if event.name == "up":
            if direcao_executada == 'b':
                return
            direcao = 'c'
        elif event.name == "down":
            if direcao_executada == 'c':
                return
            direcao = 'b'
        elif event.name == "left":
            if direcao_executada == 'd':
                return
            direcao = 'e'
        elif event.name == "right":
            if direcao_executada == 'e':
                return
            direcao = 'd'

tabuleiro = []
tamanho = 10

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append("  ")
    tabuleiro.append(linha)

    #caractere como o underline, mas mais colado na base ainda: "‾"
    #caractere como o underline, mas mais colado na base de baixo ainda: "̲"


def jogo():
    global direcao_executada

    com_protecao = False

    pontuacao = 0

    cobra = [[1, 2], [1, 3], [1, 4]]

    maca = nova_maca(cobra, tamanho)

    velocidade = 0.15

    epoch = 0
    protecao_criada = 0
    protecao_foi_criada = False

    while True:

        epoch += 1
    
        if not protecao_foi_criada: 
            protecao = []

        criar_elemento_protecao = random.randint(0, 100)

        if criar_elemento_protecao == 0 and not protecao_foi_criada and not com_protecao:
            protecao = nova_protecao(cobra, tamanho, maca)
            protecao_criada = epoch
            protecao_foi_criada = True
        
        if epoch - protecao_criada >= 20:
            protecao = []
            protecao_foi_criada = False

        limpar()

        print("Snake Game - By Daniel-Alvarenga")
        print(f"\nPontuação: {pontuacao}\n")

        print(" ┌" + " " * (tamanho * 2) + "┐")

        for i, linha in enumerate(tabuleiro):
            print(" │", end="")
            
            for j, elemento in enumerate(linha):
                if [i, j] in cobra:
                    if com_protecao:
                        print(Fore.BLUE + "██", end="")
                    else:
                        print(Fore.GREEN + "██", end="")
                elif [i, j] == maca:
                    print(Fore.RED + "██", end="")
                elif [i, j] == protecao:
                    print(Fore.YELLOW + "██", end="")
                else:
                    print(Fore.BLUE + elemento, end="")
            print(Style.RESET_ALL, end="")
            
            print("│")

        print(" └" + " " * (tamanho * 2) + "┘")


        if cobra[-1] == maca:
            cobra.insert(0, cobra[0])
            maca = nova_maca(cobra, tamanho)
            pontuacao += 1
            velocidade -= 0.001

        if cobra[-1] == protecao:
            protecao = []
            protecao_foi_criada = False
            com_protecao = True

        if cobra[-1] in cobra[:-1]:
            if com_protecao:
                com_protecao = False
            else:
                print("\nVocê perdeu se mordendo!")
                print("\nPressione para jogar novamente")
                break

        if pontuacao == tamanho ** 2 - 3:
            print("\nParabéns, você ganhou!")
            break

        if direcao == "d":
            direcao_executada = "d"
            for i, pedaco in enumerate(cobra):
                if i < len(cobra) - 1:
                    cobra[i] = cobra[i + 1]
                else:
                    if cobra[i][1] + 1 > tamanho - 1:
                        cobra[i] = [cobra[i][0], 0]
                    else:
                        cobra[i] = [cobra[i][0], cobra[i][1] + 1]

        if direcao == "e":
            direcao_executada = "e"
            for i, pedaco in enumerate(cobra):
                if i < len(cobra) - 1:
                    cobra[i] = cobra[i + 1]
                else:
                    if cobra[i][1] - 1 < 0:
                        cobra[i] = [cobra[i][0], tamanho - 1]
                    else:
                        cobra[i] = [cobra[i][0], cobra[i][1] - 1]

        if direcao == "c":
            direcao_executada = "c"
            for i, pedaco in enumerate(cobra):
                if i < len(cobra) - 1:
                    cobra[i] = cobra[i + 1]
                else:
                    if cobra[i][0] - 1 < 0:
                        cobra[i] = [tamanho - 1, cobra[i][1]]
                    else:
                        cobra[i] = [cobra[i][0] - 1, cobra[i][1]]

        if direcao == "b":
            direcao_executada = "b"
            for i, pedaco in enumerate(cobra):
                if i < len(cobra) - 1:
                    cobra[i] = cobra[i + 1]
                else:
                    if cobra[i][0] + 1 > tamanho - 1:
                        cobra[i] = [0, cobra[i][1]]
                    else:
                        cobra[i] = [cobra[i][0] + 1, cobra[i][1]]

        keyboard.on_press_key("up", pressionar_tecla)
        keyboard.on_press_key("down", pressionar_tecla)
        keyboard.on_press_key("left", pressionar_tecla)
        keyboard.on_press_key("right", pressionar_tecla)

        if keyboard.is_pressed('space'):
            print("Jogo pausado\nPressione espaço para retomar")
            keyboard.wait('space')

        print("\nMaçã:", Fore.RED + str(maca), end="")
        print(Style.RESET_ALL, end="")
        print(" Cobra: " + Fore.GREEN + str(cobra[-1]))
        print(Style.RESET_ALL, end="")

        time.sleep(velocidade)


inicio = True

while True:
    limpar()
    print(f"Snake Game - By Daniel-Alvarenga")
    
    if inicio:
        print("\nSeja bem vindo(a)!")
        print("\nPara jogar use as setas do teclado para mover a cobra e pegar as maçãs, mas cuidado para não se morder!")
        print("Para pausar SEGURE a tecla de espaço")

        iteracao = False 

    print("\nPressione ENTER para começar")

    keyboard.read_key()

    jogo()
    print("Pressione ESC para encerrar o jogo")
    if keyboard.read_key() == "esc":
        break
    else:
        pontuacao = 0
        direcao = "d"

print("\nhttps://github.com/Daniel-Alvarenga\n\nDaniel R. Alvarenga - 11/2023")
