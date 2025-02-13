from src.functions import index
from src import cursesAssets
import os
import msvcrt
import sys

# def main():
#     boas_vindas = """Para iniciar o jogo, escolha um dos desafios e pressione o numero da tecla para selecionar:
#                     pressione 1 - 1 md1
#                     pressione 2 - 2 md2
#                     pressione 3 - 3 md3
                    
#                     para cancelar pressione c"""

#     print(boas_vindas)

#     desafio_selecionado = None
#     while True:
#         try:
#             tecla = msvcrt.getch().decode()
#             match tecla:
#                 case "1":
#                     desafio_selecionado = 1
#                     break
                
#                 case "2":
#                     desafio_selecionado = 2
#                     break

#                 case "3":
#                     desafio_selecionado = 3
#                     break
                
#                 case "c":
#                     sys.exit(0)
#                     break
#         except:
#             break

#     if desafio_selecionado is not None:
#         os.system('cls')
#         game = index.CallFunction(desafio_selecionado)
#         game.escolherDesafio()

def main():
    curses_opt = cursesAssets.CursesClass([{'desc': "md1", 'value': 1}, {'desc': "md3", 'value': 2}])
    desafio_selecionado = curses_opt.opcoes(haveCancel=True)

    init_game = index.CallFunction(desafio_selecionado)
    init_game.escolherDesafio()

if __name__ == "__main__":
    main()