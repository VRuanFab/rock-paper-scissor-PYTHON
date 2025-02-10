from functions import index
import os
import keyboard
import sys


boas_vindas = """Para iniciar o jogo, escolha um dos desafios e pressione o numero da tecla para selecionar:
                pressione 1 - 1 md1
                pressione 2 - 2 md2
                pressione 3 - 3 md3
                
                para cancelar pressione c"""

print(boas_vindas)


desafio_selecionado = None
while True:
    try:
        match keyboard.read_key():
            case "1":
                desafio_selecionado = 1
                os.system('cls')
                break
            
            case "2":
                desafio_selecionado = 2
                os.system('cls')
                break

            case "3":
                desafio_selecionado = 3
                os.system('cls')
                break
            
            case "c":
                sys.exit(0)
                break
    except:
        break

if desafio_selecionado is not None:
    game = index.CallFunction(desafio_selecionado)
    game.escolherDesafio()