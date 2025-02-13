import msvcrt
import sys
import time
import random
from src import cursesAssets

class Challenge(cursesAssets.CursesClass):
    def __init__(self, challenge):
        self.challenge = challenge
        self.gameChoices = [
            {"desc": "Pedra", "value": 1},
            {"desc": "Papel", "value": 2},
            {"desc": "Tesoura", "value": 3}
            ]

        super().__init__(self.gameChoices)

    def quantidade_de_desafio(self):
        match self.challenge:
            case 1:
                self.setString(strg="md1 selecionado")
                self.challenge1()
            
            case 2:
                self.setString(strg="md3 selecionado")
                
    def machineChoice(self):
        randomChoice = random.randint(0, 2)
        return self.gameChoices[randomChoice]
    
    def quemGanhou(self):
        ##########################
        print("faz as coisas aqui")

    def challenge1(self):
        self.definirEscolhaUsuario = self.opcoes(text_before= True, header_text="Escolha o que vai jogar")
        self.escolha_maquina = self.machineChoice()

class CallFunction(Challenge):
    def __init__(self, challenge):
        self.challenge = challenge

    def escolherDesafio(self):
        super().__init__(self.challenge)
        super().quantidade_de_desafio()