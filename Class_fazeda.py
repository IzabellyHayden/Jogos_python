import random

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(40, 60)  # Nível inicial de fome aleatório
        self.tedio = random.randint(40, 60)  # Nível inicial de tédio aleatório

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

    def ouvir(self):
        print(f"{self.nome} faz barulhinhos felizes.")

    def mostrar_status(self):
        print(f"Nome: {self.nome}")
        print(f"Nível de fome: {self.fome}")
        print(f"Nível de tédio: {self.tedio}")

# Função para realizar uma ação em todos os bichinhos da fazenda
def acao_em_todos_bichinhos(fazenda, acao, argumento=None):
    for bichinho in fazenda:
        if argumento is not None:
            acao(bichinho, argumento)
        else:
            acao(bichinho)

# Função principal para interagir com a fazenda de bichinhos
def main():
    fazenda = [BichinhoVirtual(f"Bichinho{i}") for i in range(1, 6)]  # Cria 5 bichinhos na fazenda

    while True:
        print("\n----- Menu -----")
        print("1. Alimentar todos os bichinhos")
        print("2. Brincar com todos os bichinhos")
        print("3. Ouvir todos os bichinhos")
        print("4. Mostrar status de todos os bichinhos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            quantidade_comida = int(input("Quanta comida você quer dar para todos os bichinhos? "))
            acao_em_todos_bichinhos(fazenda, BichinhoVirtual.alimentar, quantidade_comida)
        elif opcao == "2":
            tempo_brincadeira = int(input("Por quanto tempo você quer brincar com todos os bichinhos? "))
            acao_em_todos_bichinhos(fazenda, BichinhoVirtual.brincar, tempo_brincadeira)
        elif opcao == "3":
            acao_em_todos_bichinhos(fazenda, BichinhoVirtual.ouvir)
        elif opcao == "4":
            acao_em_todos_bichinhos(fazenda, BichinhoVirtual.mostrar_status)
        elif opcao == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
