from colorama import Fore, Style, init
import random
import os
import time
import keyboard

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def nova_maca():
    x_maca = random.randint(0, tamanho - 1)
    y_maca = random.randint(0, tamanho - 1)

    if not [x_maca, y_maca] in cobra:
        return [x_maca, y_maca]
    else:
        return nova_maca()

direcao = "d"

def pressionar_tecla(event):
    if event.event_type == keyboard.KEY_DOWN:
        global direcao

        if event.name == "up":
            if direcao == 'b':
                return
            direcao = 'c'
        elif event.name == "down":
            if direcao == 'c':
                return
            direcao = 'b'
        elif event.name == "left":
            if direcao == 'd':
                return
            direcao = 'e'
        elif event.name == "right":
            if direcao == 'e':
                return
            direcao = 'd'
pontuacao = 0

tabuleiro = []
tamanho = 10

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append("██")
    tabuleiro.append(linha)

cobra = [[1, 2], [1, 3], [1, 4]]

maca = nova_maca()

velocidade = 0.15

while True:

    limpar()

    print(f"Snake Game - By Daniel-Alvarenga\nPontuação: {pontuacao}")

    for i, linha in enumerate(tabuleiro):
        for j, elemento in enumerate(linha):
            if [i, j] in cobra:
                print(Fore.GREEN + elemento, end="")
            elif [i, j] == maca:
                print(Fore.RED + elemento, end="")
            else:
                print(Fore.BLUE + elemento, end="")
        print("")

    print(Style.RESET_ALL, end="")

    if cobra[-1] == maca:
        cobra.insert(0, cobra[0])
        maca = nova_maca()
        pontuacao += 1
        velocidade -= 0.001

    if cobra[-1] in cobra[:-1]:
        print("Você perdeu se mordendo!")
        break

    if pontuacao == tamanho ** 2 - 3:
        print("Você ganhou!")
        break

    if direcao == 'd':
        for i, pedaco in enumerate(cobra):
            if i < len(cobra) - 1:
                cobra[i] = cobra[i + 1]
            else:
                if cobra[i][1] + 1 > tamanho - 1:
                    cobra[i] = [cobra[i][0], 0]
                else:
                    cobra[i] = [cobra[i][0], cobra[i][1] + 1]

    if direcao == 'e':
        for i, pedaco in enumerate(cobra):
            if i < len(cobra) - 1:
                cobra[i] = cobra[i + 1]
            else:
                if cobra[i][1] - 1 < 0:
                    cobra[i] = [cobra[i][0], tamanho - 1]
                else:
                    cobra[i] = [cobra[i][0], cobra[i][1] - 1]

    if direcao == 'c':
        for i, pedaco in enumerate(cobra):
            if i < len(cobra) - 1:
                cobra[i] = cobra[i + 1]
            else:
                if cobra[i][0] - 1 < 0:
                    cobra[i] = [tamanho - 1, cobra[i][1]]
                else:
                    cobra[i] = [cobra[i][0] - 1, cobra[i][1]]

    if direcao == 'b':
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

    print(maca, cobra[-1])

    time.sleep(velocidade)
