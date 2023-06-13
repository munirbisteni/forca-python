import sorteador
import forca
import teclado
import time
import threading
import sys
import os

sortear = sorteador.Sorteador()
forcaJogo = forca.Forca()
pegaTeclado = teclado.Teclado()
class jogar:
    def __init__(self) -> None:
        forcaJogo.__init__()
        self.palavra = ""
        self.palavraTracos = ""
        self.minutos = 0
        self.errosDisponiveis = 0
        self.segundos_restantes = 0
        self.palavraAtualizacao = []
        self.menu()
        

    def contagem_regressiva(self):
        total_minutos = 1
        total_segundos = total_minutos * 60
        for segundos in range(total_segundos, 0, -1):
            self.minutos = segundos // 60
            self.segundos_restantes = segundos % 60
            time.sleep(1)
        print("\nTempo esgotado!")
        self.fim()


    def menu(self):
        digito = 4
        os.system('cls')
        print(f"""
        -=============== Menu ===============-
        1 - Jogar!
        2 - Escolher palavra para próximo jogo! 
        3 - Desligar!
        -====================================-
        """)
        while digito > 3:
            print("Escolha um digito entre 1 e 3!")
            digito = pegaTeclado.pegaDigito()
        if digito == 1:
            print("\n")
            self.iniciarJogo()
        elif digito == 2:
            self.jogoDoUsuario()
        elif digito == 3:
            self.sair()
            
    def iniciarJogo(self):
        palavraTemp = sortear.sortearPalavra()
        self.palavra = forcaJogo.armazenaPalavra(palavraTemp)
        self.palavraTracos = forcaJogo.embaralhaPalavra()
        self.errosDisponiveis = forcaJogo.errosDisponiveis(forcaJogo._palavra())
        self.visor()

 
    def jogoDoUsuario(self):
        palavraTemp = pegaTeclado.pegaPalavra()
        self.palavra = forcaJogo.armazenaPalavra(palavraTemp)
        self.palavraTracos = forcaJogo.embaralhaPalavra()
        self.errosDisponiveis = forcaJogo.errosDisponiveis(forcaJogo._palavra())
        self.visor()

    def visor(self):
        threading.Thread(target=self.contagem_regressiva).start()
        self.palavraAtualizacao = [self.palavraTracos, "-", "-"]
        while  self.errosDisponiveis >= 0 and self.palavraAtualizacao[0] != forcaJogo._palavra():
            os.system('cls')   
            print(f"""A palavra da vez é: \n {forcaJogo.forcaErros(self.errosDisponiveis)} \n {self.palavraAtualizacao[0]} \n {self.errosDisponiveis} tentativas disponíveis \n Contagem regressiva: {self.minutos:02d}:{self.segundos_restantes:02d} \n Erros: {self.palavraAtualizacao[2]} \n para sair escreva "#"
            """)
            self.palavraAtualizacao = forcaJogo.descobrir(self.palavraAtualizacao)
            if self.palavraAtualizacao[3] == "#":
                self.fim()
                break

            if self.palavraAtualizacao[1] == True:
                self.errosDisponiveis -= 1
        
        if self.errosDisponiveis < 0 or self.palavraAtualizacao[0] ==forcaJogo._palavra():
            self.fim()

    def fim(self):
        os.system('cls') 
        if self.errosDisponiveis < 0 or self.palavraAtualizacao[0] != forcaJogo._palavra():
            print("Voce perdeu!")
            print(f"a palavra era: {forcaJogo._palavra()}")
        else:
            print(f"voce ganhou, a palavra era: {forcaJogo._palavra()}")
        resposta = ""
        while resposta != "s" and resposta != "n":
           print("Deseja tentar novamente? S/N")
           resposta = pegaTeclado.pegaChar().lower()

        if resposta == "s":
            self.__init__()
        if resposta == "n":
            self.sair()

    def sair(self):
        print("Obrigado por jogar!")
        sys.exit(0)
        
if __name__ == '__main__':
    jogada = jogar()
