class Challenge:
    def __init__(self, challenge):
        self.challenge = challenge

    def quantidade_de_desafio(self):
        match self.challenge:
            case 1:
                print("desafio 1 selecionado")
                # self.tutorial()
                self.challenge1()
            
            case 2:
                print("desafio 2 selecionado")

            case 3:
                print("desafio 3 selecionado")

    def definirResultado(self, valor):
        self.response = valor

    def tutorial(self):
        return print("tutorial")

    def challenge1(self):
        print("hellooooou")
        return self.tutorial()


class CallFunction(Challenge):
    def __init__(self, challenge):
        self.challenge = challenge

    def escolherDesafio(self):
        super().__init__(self.challenge)
        super().quantidade_de_desafio()