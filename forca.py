import teclado
pegaTeclado = teclado.Teclado()
class Forca:
    def __init__(self) -> None:
        self.palavraJogo = []
        self.tracos = ""
        self.listaErros = ["-"]

    def armazenaPalavra(self, palavra) -> str:
        result = []
        for a in palavra:
            a = a.lower()
            if a == " ":
                char ={a:" "}
            else:
                char = {a:"_"}
            result.append(char)
        self.palavraJogo = result
        return result
    
    def embaralhaPalavra(self) -> str:
        tracos =""
        for i in range(0,len(self.palavraJogo)):
            for v in self.palavraJogo[i].values():
                tracos += v
        self.tracos = tracos
        return tracos
    
    
    def descobrir(self, palavraTracosIndexada):
        char = pegaTeclado.pegaChar()
        self.listaErros.append(char)
        self.tracos = palavraTracosIndexada[0] 
        retorno = ""
        erro = True
        for i in  range(0,len(self.palavraJogo)):
            for k in self.palavraJogo[i].keys():
                if char == k:
                   erro = False
                   retorno += char
                   if self.listaErros[-1] == char:
                       self.listaErros.pop()
                elif k == " ":
                    retorno += " "
                elif self.tracos[i] != "_":
                    retorno += self.tracos[i]
                else:
                    retorno += "_"
        return retorno, erro, self.organizaErros(), char

    def errosDisponiveis(self, palavraSorteada) -> int:
        erros = round((len(palavraSorteada))*0.4)
        if erros < 6:
            erros = 6
        return erros      
    
    def boneQuinhoForca(self) -> str:
        pass

    def _palavra(self) -> str:
        result = ""
        for i in range(0,len(self.palavraJogo)):
            for k in self.palavraJogo[i].keys():
                result += k
        return result
    
    def organizaErros(self) -> str:
        retorno = f""
        for a in self.listaErros:
            retorno += f"{a} "
        return retorno
    
    def forcaErros(self, errosDisponiveis) -> str:
        if errosDisponiveis >= 6:
            return """_______\n|      |\n|      \n|     \n|     
            """
        elif errosDisponiveis == 5:
            return """_______\n|      |\n|      0\n|     \n|     
            """

        elif errosDisponiveis == 4:
            return """_______\n|      |\n|      0\n|      |\n|     
            """
        
        elif errosDisponiveis == 3:
            return """_______\n|      |\n|      0\n|     /|\n|     
            """
        elif errosDisponiveis == 2:
            return """_______\n|      |\n|      0\n|     /|\\\n|     
            """
        elif errosDisponiveis == 1:
            return """_______\n|      |\n|      0\n|     /|\\\n|     / 
            """
        elif errosDisponiveis == 0:
            return """_______\n|      |\n|      0\n|     /|\\\n|     / \\
            """