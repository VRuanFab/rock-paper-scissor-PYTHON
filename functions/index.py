import msvcrt
import sys

class Challenge:
    def __init__(self, challenge):
        self.challenge = challenge

    def quantidade_de_desafio(self):
        match self.challenge:
            case 1:
                print("desafio 1 selecionado")
                self.challenge1()
            
            case 2:
                print("desafio 2 selecionado")

            case 3:
                print("desafio 3 selecionado")

    def definirEscolhaUsuario(self, valor):
        self.escolhaUsuario = valor

    def tutorial(self):
        print("escolha sua jogada")
        return print("""
1 - pedra
2 - papel
3 - tesoura
""")

    def challenge1(self):
        self.tutorial()
        
        while True:
            try:
                tecla = msvcrt.getch().decode()
                match tecla:
                    case "1":
                        self.definirEscolhaUsuario("pedra")
                        break
                    
                    case "2":
                        self.definirEscolhaUsuario("papel")
                        break
                    
                    case "3":
                        self.definirEscolhaUsuario("tesoura")
                        break
            except:
                pass

        print(f"sua escolha foi {self.escolhaUsuario}")
        print("programa encerrado até o momento, pressione qualquer tecla para finalizar")
        if msvcrt.getch():
            sys.exit(0)

class CallFunction(Challenge):
    def __init__(self, challenge):
        self.challenge = challenge

    def escolherDesafio(self):
        super().__init__(self.challenge)
        super().quantidade_de_desafio()