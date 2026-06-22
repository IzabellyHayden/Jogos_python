class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto: ({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


# Função para imprimir o centro do retângulo
def imprimirCentro(retangulo):
    centro = retangulo.encontrarCentro()
    print(f"Centro do retângulo: ({centro.x}, {centro.y})")


# Função principal
def main():
    ponto_inicio = Ponto(x=0, y=0)
    retangulo = Retangulo(ponto_inicio, largura=5, altura=3)

    while True:
        print("\n----- Menu -----")
        print("1. Imprimir Ponto de Início do Retângulo")
        print("2. Imprimir Centro do Retângulo")
        print("3. Alterar Valores do Retângulo")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ponto_inicio.imprimir()
        elif opcao == "2":
            imprimirCentro(retangulo)
        elif opcao == "3":
            novo_x = float(input("Digite o novo valor de x para o ponto inicial: "))
            novo_y = float(input("Digite o novo valor de y para o ponto inicial: "))
            retangulo.ponto_inicial = Ponto(novo_x, novo_y)
            novo_largura = float(input("Digite a nova largura do retângulo: "))
            novo_altura = float(input("Digite a nova altura do retângulo: "))
            retangulo.largura = novo_largura
            retangulo.altura = novo_altura
            print("Valores do retângulo atualizados.")
        elif opcao == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
