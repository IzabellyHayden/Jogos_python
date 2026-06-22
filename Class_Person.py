class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            # A cada ano que a pessoa envelhece e tem menos de 21 anos, ela cresce 0,5 cm
            self.crescer(0.5 * anos)

    def engordar(self, peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def crescer(self, altura_ganha):
        self.altura += altura_ganha

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} cm")

# Exemplo de uso da classe Pessoa
pessoa1 = Pessoa(nome="Alice", idade=18, peso=60, altura=165)
pessoa1.mostrar_informacoes()

pessoa1.envelhecer(2)
pessoa1.engordar(5)
pessoa1.emagrecer(3)
pessoa1.mostrar_informacoes()
