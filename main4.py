from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente
from datetime import datetime

def solicitar_confirmacao(mensagem):
    """Solicita uma resposta do tipo S ou N e valida."""
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta.isalpha() and resposta in ['S', 'N']:
            return resposta
        else:
            print("❌ Entrada inválida. Por favor, digite apenas 'S' para sim ou 'N' para não.\n")


def criar_contas():
    """Cria conta-corrente e conta poupança integradas."""
    print("\n🎉 Ótimo! Vamos começar o processo para abrir sua conta.")

    nome = input('Nome: ')

    while True:
        data_nascimento_input = input('Data nascimento (dd/mm/aaaa): ')
        try:
            data_nascimento = datetime.strptime(data_nascimento_input, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato inválido! Use o formato dd/mm/aaaa.")

    email = input('E-mail: ')

    # Criando instância de ContaCorrente
    conta_corrente = ContaCorrente(
        nome=nome,
        data_nascimento=data_nascimento,
        email=email
    )

    # Criando instância de ContaPoupanca integrada
    conta_poupanca = ContaPoupanca(
        nome=conta_corrente.nome,
        data_nascimento=conta_corrente.data_nascimento,
        email=conta_corrente.email
    )

    print("\nConta corrente criada com Sucesso! ✅")
    conta_corrente.imprimir_dados()

    print("\nFoi criada também uma conta poupança integrada à sua conta! ✅")
    conta_poupanca.imprimir_dados()

    return conta_corrente, conta_poupanca
def realizar_deposito(conta_corrente):
    """Pergunta e executa depósito na conta corrente."""
    resposta = solicitar_confirmacao("💬 Deseja realizar depósitos? (S - sim | N - não): ")
    if resposta == 'S':
        print("\n🎉 Ótimo! Vamos começar o processo de depósitos na conta.")
        valor = float(input('Informe o valor do depósito: '))
        conta_corrente.deposito(valor)
    else:
        print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")

def realizar_transferencia(conta_corrente, conta_poupanca) -> None:
    """Pergunta e executa transferência da conta corrente para poupança."""
    resposta = solicitar_confirmacao("💬 Deseja realizar transferência para a poupança? (S - sim | N - não): ")
    if resposta == 'S':
        valor = float(input('Informe o valor da transferência: '))
        conta_corrente.transfere(valor=valor)
        conta_poupanca.receber_transferencia(valor=valor)
        conta_poupanca.saldo_conta_cp()
    else:
        print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")

def consulta_saldo(conta_corrente) -> None:
    """Pergunta e executa a consulta do saldo na conta corrente."""
    resposta = solicitar_confirmacao("💬 Deseja consultar o saldo da conta corrente? (S - sim | N - não): ")
    if resposta == 'S':
        conta_corrente.mostrar_saldo()
    else:
        print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")

def solicitar_emprestimo(conta_corrente) -> None:
    """Pergunta e executa a solicitação de empréstimos."""
    resposta = solicitar_confirmacao("💬 Deseja solicitar empréstimos? (S - sim | N - não): ")
    if resposta == 'S':
        conta_corrente.emprestimo(
            valor=float(input('Qual o valor que deseja: ')),
            parcela=int(input('Informe o número de parcelas a pagar: '))
        )
    else:
        print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")

def solicita_cheque_especial(conta_corrente) -> None:
    """Pergunta e executa a solicitação de cheque especial."""
    resposta = solicitar_confirmacao("💬 Deseja solicitar o valor do cheque especial? (S - sim | N - não): ")
    if resposta == 'S':
        conta_corrente.chequeEsp()
    else:
        print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")

def consulta_saldo_poupanca(conta_poupanca) -> None:
    """Pergunta e executa a consulta na poupança."""
    resposta = solicitar_confirmacao('💬 Deseja consultar o saldo na conta poupança? (S - sim | N - não): ')
    if resposta == 'S':
        conta_poupanca.saldo_conta_cp()
    else:
        print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")

def simular_rendimento_poupanca(conta_poupanca) -> None:
    """Pergunta e executa a simulação de rendimento na poupança."""
    resposta = solicitar_confirmacao('💬 Deseja simular o rendimento da poupança? (S - sim | N - não): ')
    if resposta == 'S':
        meses = int(input('Informe o período em meses para a simulação: '))
        conta_poupanca.simular_rendimento(meses)
    else:
        print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")

def calcular_rendimento_poupanca(conta_poupanca) -> None:
    """Pergunta e executa o cálculo de rendimento na poupança."""
    resposta = solicitar_confirmacao('💬 Deseja calcular o rendimento da poupança? (S - sim | N - não): ')
    if resposta == 'S':
        meses = int(input('Informe o período em meses para o cálculo: '))
        rendimento = conta_poupanca.calcular_rendimento(meses)
        print(f'\n💰 Rendimento calculado: R$ {rendimento:.2f}')
    else:
        print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")


from datetime import datetime

def atualizar_dados(conta_corrente, conta_poupanca) -> None:
    """Pergunta e executa a atualização de dados pessoais."""
    resposta = solicitar_confirmacao('💬 Deseja atualizar os seus dados pessoais? (S - sim | N - não): ')

    if resposta == 'S':
        print("\n📝 Vamos atualizar seus dados.")

        # Atualizar nome
        print(f"📌 Nome atual: {conta_corrente.nome}")
        novo_nome = input("Digite o novo nome (ou Enter para manter o atual): ").strip()
        if novo_nome:
            conta_corrente.nome = novo_nome
            conta_poupanca.nome = novo_nome

        # Atualizar data de nascimento
        print(f"📅 Data de nascimento atual: {conta_corrente.data_nascimento.strftime('%d/%m/%Y')}")
        nova_data = input("Digite a nova data de nascimento (formato: dd/mm/aaaa ou Enter para manter a atual): ").strip()
        if nova_data:
            try:
                nova_data_dt = datetime.strptime(nova_data, "%d/%m/%Y")
                conta_corrente.data_nascimento = nova_data_dt
                conta_poupanca.data_nascimento = nova_data_dt
            except ValueError:
                print("❌ Data inválida! Use o formato dd/mm/aaaa. Data de nascimento não foi alterada.")

        # Atualizar e-mail
        print(f"📧 E-mail atual: {conta_corrente.email}")
        novo_email = input("Digite o novo e-mail (ou Enter para manter o atual): ").strip()
        if novo_email:
            conta_corrente.email = novo_email
            conta_poupanca.email = novo_email

        print("\n✅ Dados atualizados com sucesso!")
        conta_corrente.imprimir_dados()
        conta_poupanca.imprimir_dados()
    else:
        print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")


"""Fluxo principal do programa."""
def main():
    resposta = solicitar_confirmacao("💬 Deseja abrir uma conta? (S - sim | N - não): ")
    if resposta == 'S':
        conta_corrente, conta_poupanca = criar_contas()

        while True:
            print("\n📋 MENU DE OPERAÇÕES:")
            print("1 - Depósitos")
            print("2 - Transferência para poupança")
            print("3 - Consulta saldo conta corrente")
            print("4 - Consulta saldo poupança")
            print("5 - Solicitar empréstimo")
            print("6 - Solicitar cheque especial")
            print("7 - Simular rendimento poupança")
            print("8 - Calcular rendimento poupança")
            print("9 - Atualizar dados pessoais")
            print("0 - Sair")

            opcao = input("👉 Informe a opção desejada: ")

            match opcao:
                case '1':
                    realizar_deposito(conta_corrente)
                case '2':
                    realizar_transferencia(conta_corrente, conta_poupanca)
                case '3':
                    conta_corrente.mostrar_saldo()
                case '4':
                    conta_poupanca.saldo_conta_cp()
                case '5':
                    solicitar_emprestimo(conta_corrente)
                case '6':
                    solicita_cheque_especial(conta_corrente)
                case '7':
                    simular_rendimento_poupanca(conta_poupanca)
                case '8':
                    calcular_rendimento_poupanca(conta_poupanca)
                case '9':
                    atualizar_dados(conta_corrente, conta_poupanca)
                case '0':
                    print("\n👋 Encerrando o sistema. Obrigado por utilizar nossos serviços!")
                    break
                case _:
                    print("❌ Opção inválida. Por favor, tente novamente.")
    else:
        print("👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")

# Executa o programa
if __name__ == "__main__":
    main()