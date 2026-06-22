class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornarLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)

# Programa principal
def main():
    # Solicita as medidas do local ao usuário
    comprimento = float(input("Informe o comprimento do local: "))
    largura = float(input("Informe a largura do local: "))

    # Cria um objeto da classe Retangulo com as medidas informadas
    local = Retangulo(ladoA=comprimento, ladoB=largura)

    # Calcula a quantidade de pisos e rodapés necessários
    area_local = local.calcularArea()
    perimetro_local = local.calcularPerimetro()

    area_piso = float(input("Informe a área de cada piso: "))
    altura_rodape = float(input("Informe a altura de cada rodapé: "))

    quantidade_pisos = area_local / area_piso
    quantidade_rodapes = perimetro_local / altura_rodape

    print("\nQuantidade de pisos necessários:", quantidade_pisos)
    print("Quantidade de rodapés necessários:", quantidade_rodapes)

if __name__ == "__main__":
    main()
