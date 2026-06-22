class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}!")

    def verBucho(self):
        if self.bucho:
            print(f"{self.nome} tem no estômago: {', '.join(self.bucho)}")
        else:
            print(f"{self.nome} está com o estômago vazio.")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo...")
            self.bucho = []
            print(f"{self.nome} terminou de digerir. Estômago vazio.")
        else:
            print(f"{self.nome} não tem nada no estômago para digerir.")

# Programa principal
macaco1 = Macaco(nome="Chico")
macaco2 = Macaco(nome="Bola")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Nozes")

macaco2.comer("Peixe")
macaco2.comer("Folhas")
macaco2.comer("Frutas")

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir()
macaco2.digerir()

# Tentativa de fazer um macaco comer o outro
macaco1.comer(macaco2)
macaco1.verBucho()
