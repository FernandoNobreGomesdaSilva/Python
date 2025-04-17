from Banco import Banco

class ContaPoupanca(Banco):
    def __init__(self, nome: str, data_nascimento: str, email: str) -> None:
        """
        Inicializa uma conta poupança com taxa de juros básica.
        """
        self._juros = 0.005  # 0.5% ao mês
        super().__init__(nome, data_nascimento, email)
        # Garantir que saldo inicial seja zero
        self._saldo_conta_poupanca = 0

    def receber_transferencia(self, valor: float) -> None:
        """Recebe uma transferência da conta-corrente."""
        if valor <= 0:
            raise ValueError("Valor da transferência deve ser positivo")
        self._saldo_conta_poupanca += valor
        print(f"✅ Transferência de R$ {valor:.2f} recebida na poupança")

    def calcular_rendimento(self, meses: int) -> float:
        """
        Calcula o rendimento com juros compostos.

        Args:
            meses: Período em meses

        Returns:
            Valor do rendimento
        """
        if meses <= 0:
            raise ValueError("Período deve ser positivo")

        if self._saldo_conta_poupanca <= 0:
            return 0.0

        return self._saldo_conta_poupanca * ((1 + self._juros) ** meses - 1)

    def simular_rendimento(self, meses: int) -> None:
        """Mostra projeção de rendimento."""
        try:
            rendimento = self.calcular_rendimento(meses)
            total = self._saldo_conta_poupanca + rendimento

            print("\n📈 Simulação de Rendimento")
            print(f"Saldo atual: R$ {self._saldo_conta_poupanca:.2f}")
            print(f"Taxa de juros: {self._juros * 100:.2f}% a.m.")
            print(f"Período: {meses} meses")
            print(f"Rendimento: R$ {rendimento:.2f}")
            print(f"Total projetado: R$ {total:.2f}")

        except ValueError as e:
            print(f"❌ Erro: {e}")

    def imprimir_dados(self) -> None:
        """Exibe informações da conta."""
        print("\n" + "=" * 50)
        print("🏦 CONTA POUPANÇA".center(50))
        super().imprimir_dados()
        print(f"💰 Saldo: R$ {self._saldo_conta_poupanca:.2f}")
        print(f"📈 Juros: {self._juros * 100:.2f}% a.m.")
        print("=" * 50)