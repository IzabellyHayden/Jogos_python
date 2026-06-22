class TV:
    def __init__(self):
        self.canal = 1  # Canal inicial
        self.volume = 50  # Volume inicial

    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            print(f"Canal alterado para {novo_canal}")
        else:
            print("Canal inválido. Deve estar entre 1 e 100.")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume máximo atingido.")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume mínimo atingido.")

    def mostrarStatus(self):
        print(f"Canal: {self.canal}")
        print(f"Volume: {self.volume}")

# Programa principal
def main():
    televisao = TV()

    while True:
        print("\n----- Menu -----")
        print("1. Mudar Canal")
        print("2. Aumentar Volume")
        print("3. Diminuir Volume")
        print("4. Mostrar Status")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_canal = int(input("Informe o novo número do canal: "))
            televisao.mudarCanal(novo_canal)
        elif opcao == "2":
            televisao.aumentarVolume()
        elif opcao == "3":
            televisao.diminuirVolume()
        elif opcao == "4":
            televisao.mostrarStatus()
        elif opcao == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
