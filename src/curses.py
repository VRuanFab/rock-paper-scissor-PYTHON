import curses

class CursesClass:
    def __init__(self, options):
        self.options= options
        self.indice = 0
        
        stdscr = curses.initscr()
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        
        self.inpt = stdscr
        
    def opcoes(self):
        self.options.append("cancelar")
        curses.curs_set(0)
        inpt = self.inpt
        inpt.nodelay(False)
        inpt.timeout(100)
        
        while True:
            inpt.clear()
            inpt.addstr(0, 0, "Use ↑ ↓ para navegar e Enter para selecionar\n", curses.A_BOLD)
            
            for i, opcao in enumerate(self.options):
                if i == self.indice:
                    inpt.addstr(i + 2, 0, f" > {opcao}", curses.A_BOLD | curses.color_pair(1)) if opcao != "cancelar" else inpt.addstr(i + 2, 0, f"-- {opcao} --", curses.A_BOLD | curses.color_pair(3))
                    
                elif opcao == "cancelar":
                    inpt.addstr(i + 2, 0, f"-- {opcao} --", curses.color_pair(2))
                    
                else:
                    inpt.addstr(i + 2, 0, f" {opcao}")

            tecla = inpt.getch()
            
            if tecla == curses.KEY_UP:
                self.indice = (self.indice - 1) % len(self.options)
                print(self.indice)
            elif tecla == curses.KEY_DOWN:
                self.indice = (self.indice + 1) % len(self.options)
                print(self.indice)
            elif tecla == 10:
                return self.options[self.indice]