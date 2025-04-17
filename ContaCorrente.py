from Banco import Banco


class ContaCorrente(Banco):
    contador_contas = 0  # Variável de classe para contar as contas
    creditoEmprestimo = 10000.00
    jurosEmprestimo = 0.01  # 1% ao mês
    chequeEspecial = 2500.00
    jurosChequeEspecial = 0.015  # 1.5% ao mês

    def __init__(self, nome: str, data_nascimento: str, email: str) -> None:
        # Incrementa o contador de contas corretamente (usando a classe)
        ContaCorrente.contador_contas += 1
        self.__numeroConta = ContaCorrente.contador_contas
        super().__init__(nome, data_nascimento, email)
        self._saldo_conta_corrente = 0  # Inicializado no Banco, mas pode ser redefinido aqui

    def emprestimo(self, valor: float, parcela: int) -> None:
        """Realiza um empréstimo com juros."""
        if valor <= 0:
            print("❌ Valor do empréstimo deve ser positivo!")
            return

        if self.creditoEmprestimo == 0 or valor > self.creditoEmprestimo:
            print(f'❌ Crédito disponível: R$ {self.creditoEmprestimo:.2f} - Operação não realizada!')
            return

        # Calcula o valor total com juros
        valor_total = valor * (1 + self.jurosEmprestimo)
        valor_parcela = valor_total / parcela

        # Atualiza saldos
        self._saldo_conta_corrente += valor
        self.creditoEmprestimo -= valor

        print(f'\n💰 Empréstimo concedido: R$ {valor:.2f}')
        print(f'📈 Valor total a pagar: R$ {valor_total:.2f} (juros de {self.jurosEmprestimo * 100}% a.m.)')
        print(f'📅 {parcela} parcelas de R$ {valor_parcela:.2f}')
        print(f'💳 Saldo atual na conta: R$ {self._saldo_conta_corrente:.2f}')
        print(f'🏦 Crédito restante: R$ {self.creditoEmprestimo:.2f}')

    def chequeEsp(self) -> None:
        """Mostra informações sobre o cheque especial."""
        if self.chequeEspecial <= 0:
            print('❌ Cheque especial indisponível no momento.')
            return

        valor_juros = self.chequeEspecial * self.jurosChequeEspecial
        valor_total = self.chequeEspecial + valor_juros

        print('\n💳 Cheque Especial:')
        print(f'💰 Limite disponível: R$ {self.chequeEspecial:.2f}')
        print(f'📈 Juros: {self.jurosChequeEspecial * 100}% a.m.')
        print(f'⚠️  Valor total em caso de uso: R$ {valor_total:.2f}')

    def mostrar_saldo(self) -> None:
        """Exibe saldo total (conta + cheque especial)."""
        saldo_total = self._saldo_conta_corrente + self.chequeEspecial
        print('\n📊 Saldos:')
        print(f'💳 Conta corrente: R$ {self._saldo_conta_corrente:.2f}')
        print(f'🏦 Cheque especial: R$ {self.chequeEspecial:.2f}')
        print(f'💰 Total disponível: R$ {saldo_total:.2f}')

    def imprimir_dados(self) -> None:
        """Mostra informações da conta."""
        print("\n" + "=" * 50)
        print("💳 CONTA CORRENTE".center(50))
        print(f"📋 Número: {self.__numeroConta}")
        super().imprimir_dados()
        print(f"💵 Saldo: R$ {self._saldo_conta_corrente:.2f}")
        print("=" * 50)

    @property
    def numeroConta(self) -> int:
        """Getter para o número da conta."""
        return self.__numeroConta