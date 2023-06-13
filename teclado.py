class Teclado:
    def __init__(self) -> None:
        pass

    def pegaChar(self) -> str:
        char = ""
        verificador = 0
        while verificador == 0:
            char = input("Insira a próxima letra: ")
            if len(char) > 1:
                print("Tamanho inválido, tente novamente! ")
            if char.isalpha():
                verificador = 1
            if char == "#":
                verificador = 1
            if not char.isalpha():
                print("são aceitas apenas letras! ")
        return char
    
    def pegaDigito(self) -> int:
        digito = 0
        verificador = 0
        while verificador == 0:
            try:
                digito = int(input("Insira o digito: "))
            except ValueError:
                print("Inválido, apenas números!")
            verificaDigito = str(digito)
            if len(verificaDigito) > 1:
                print("Apenas digitos de 0 a 9")
            elif verificaDigito.isdigit():
                verificador = 1
        return digito

    def pegaPalavra(self) -> str:
        verificador = 0
        while verificador == 0:
            retorno = input("Insira a palavra, sem caractéres especiais:")
            for i in range(0,len(retorno)):
                if retorno[i].isalpha() or retorno[i] == " ":
                    verificador = 1
                else:
                    verificador = 0
                    break
        return retorno


             
    def converterLower(self, toLower) -> str:
        saida = ""
        try:
            saida = toLower.lower()
        except AttributeError:
            print("Tipo inválido para função lower!")
        return saida
            
    