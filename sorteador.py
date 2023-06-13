import random
class Sorteador:
    
    def __init__(self):
        self.palavras = ["Trofosilda","Computador","Colegio","Vespertino","E o vento levou","Matrix","Harry Potter","Julio", "a pedra filosofal", "queijo prato", "marreco"]
        
    def sortearPalavra(self) -> str:
        palavraSorteada = random.choice(self.palavras)
        return palavraSorteada