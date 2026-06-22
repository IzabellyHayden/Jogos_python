class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade_comida):
        if quantidade_comida > 0:
            self.fome -= quantidade_comida
            print(f"{self.nome} comeu. Nível de fome reduzido.")
        else:
            print("Quantidade de comida inválida. Nenhum efeito.")

    def brincar(self, tempo_brincadeira):
        if tempo_brincadeira > 0:
            self.tedio -= tempo_brincadeira
            print(f"{self.nome} brincou. Nível de tédio reduzido.")
        else:
            print("Tempo de brincadeira inválido. Nenhum efeito.")

    def mostrar_status(self):
        print(f"Nome: {self.nome}")
        print(f"Nível de fome: {self.fome}")
        print(f"Nível de tédio: {self.tedio}")


# Exemplo de uso da classe BichinhoVirtual
meu_bichinho = BichinhoVirtual(nome="Fofinho")

meu_bichinho.mostrar_status()

quantidade_comida = int(input("Quanta comida você quer dar para o bichinho? "))
tempo_brincadeira = int(input("Por quanto tempo você quer brincar com o bichinho? "))

meu_bichinho.alimentar(quantidade_comida)
meu_bichinho.brincar(tempo_brincadeira)

meu_bichinho.mostrar_status()
