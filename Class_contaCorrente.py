class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        elif valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def mostrarSaldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# Exemplo de uso da classe ContaCorrente
conta1 = ContaCorrente(numero_conta="12345", nome_correntista="João")

conta1.mostrarSaldo()

conta1.deposito(1000)
conta1.mostrarSaldo()

conta1.saque(500)
conta1.mostrarSaldo()

conta1.alterarNome("João Silva")
print("Novo nome do correntista:", conta1.nome_correntista)
