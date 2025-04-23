from datetime import datetime

class Banco:
    # Constructor
    def __init__(self, nome: str, data_nascimento: datetime, email: str) -> None:
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._email = email
        self._saldo_conta_corrente = 0
        self._saldo_conta_poupanca = 0
        self.valor = 0

    # Getters e Setters para nome, data_nascimento e email (estão corretos)
    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def data_nascimento(self) -> datetime:
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: datetime) -> None:
        self._data_nascimento = data_nascimento

    @property
    def email(self) -> str:
        return self.email

    @email.setter
    def email(self, email: str) -> None:
        self.email = email

    # Métodos para operações financeiras (todos corretos)
    def deposito(self, valor: float) -> float:
        print(f' 💰 Depósito no valor de: R$ {valor:.2f} realizado com sucesso na conta corrente')
        self._saldo_conta_corrente += valor
        return self._saldo_conta_corrente

    def transfere(self, valor: float):
        if self._saldo_conta_corrente >= valor:
            self._saldo_conta_corrente -= valor
            self._saldo_conta_poupanca += valor
            print(f' 💰 Transferência de R$ {valor:.2f} para a conta poupança realizada com sucesso.')
        elif valor == 0 or valor == "":
            print(" ❌ Operação não realizada")
        else:
            print(' 💰 Saldo insuficiente na conta corrente para transferência.')
        return self._saldo_conta_corrente, self._saldo_conta_poupanca

    def saldo_conta_cc(self) -> float:
        print(f' 💰 Saldo na C/C: R$ {self._saldo_conta_corrente:.2f}')
        return self._saldo_conta_corrente

    def saldo_conta_cp(self) -> float:
        print(f' 💰 Saldo na poupança: R$ {self._saldo_conta_poupanca:.2f}')
        return self._saldo_conta_poupanca

    def atualiza_saldo(self, valor: float) -> float:
        self._saldo_conta_corrente -= valor
        print(f' 💰 Saldo atualizado. Novo saldo na C/C: R$ {self._saldo_conta_corrente:.2f}')
        return self._saldo_conta_corrente

    def imprimir_dados(self) -> None:
        print(f' 👤 Nome: {self.nome}')
        print(f' 📧 E-mail: {self.email}')
        if isinstance(self.data_nascimento, datetime):
            data_formatada = self.data_nascimento.strftime("%d/%m/%Y")
        else:
            data_formatada = str(self.data_nascimento)  # fallback simples
        print(f' 📅 Data de Nascimento: {data_formatada}')