class BichinhoVirtual:
    def __init__(self, nome, fome=50, saude=50, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, novo_nivel_fome):
        self.fome = max(0, min(100, novo_nivel_fome))

    def alterarSaude(self, novo_nivel_saude):
        self.saude = max(0, min(100, novo_nivel_saude))

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def calcularHumor(self):
        humor = (self.fome + self.saude) / 2
        return humor

# Exemplo de uso da classe BichinhoVirtual
meu_bichinho = BichinhoVirtual(nome="Tama")

print(f"Nome: {meu_bichinho.retornarNome()}")
print(f"Fome: {meu_bichinho.retornarFome()}")
print(f"Saúde: {meu_bichinho.retornarSaude()}")
print(f"Idade: {meu_bichinho.retornarIdade()}")
print(f"Humor: {meu_bichinho.calcularHumor()}")

meu_bichinho.alterarFome(80)
meu_bichinho.alterarSaude(60)
meu_bichinho.alterarIdade(1)

print(f"\nNovo estado do bichinho:")
print(f"Fome: {meu_bichinho.retornarFome()}")
print(f"Saúde: {meu_bichinho.retornarSaude()}")
print(f"Idade: {meu_bichinho.retornarIdade()}")
print(f"Humor: {meu_bichinho.calcularHumor()}")
