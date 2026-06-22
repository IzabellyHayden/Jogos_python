class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

# Exemplo de uso da classe Bola
minha_bola = Bola(cor="azul", circunferencia=30, material="couro")

print("Cor atual da bola:", minha_bola.mostraCor())

minha_bola.trocaCor("vermelho")

print("Nova cor da bola:", minha_bola.mostraCor())
