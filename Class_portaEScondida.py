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

    def __str__(self):
        return f"BichinhoVirtual(nome='{self.nome}', fome={self.fome}, tedio={self.tedio})"


# Exemplo de uso da classe BichinhoVirtual com opção secreta
meu_bichinho = BichinhoVirtual(nome="Fofinho")

while True:
    print("\n----- Menu -----")
    print("1. Alimentar o bichinho")
    print("2. Brincar com o bichinho")
    print("3. Mostrar status do bichinho")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        quantidade_comida = int(input("Quanta comida você quer dar para o bichinho? "))
        meu_bichinho.alimentar(quantidade_comida)
    elif opcao == "2":
        tempo_brincadeira = int(input("Por quanto tempo você quer brincar com o bichinho? "))
        meu_bichinho.brincar(tempo_brincadeira)
    elif opcao == "3":
        meu_bichinho.mostrar_status()
    elif opcao == "0":
        print("Saindo do programa.")
        break
    elif opcao == "senha_secreta":  # Opção secreta para mostrar os valores exatos dos atributos
        print("Opção secreta escolhida. Exibindo valores exatos:")
        print(str(meu_bichinho))
    else:
        print("Opção inválida. Tente novamente.")
