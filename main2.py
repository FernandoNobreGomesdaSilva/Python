from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente

# Criando um objeto e testando
while True:
    resposta = input("💬 Deseja abrir uma conta? (S - sim | N - não): ").strip().upper()

    if resposta.isalpha() and resposta in ['S', 'N']:
        if resposta == 'S':
            print("\n🎉 Ótimo! Vamos começar o processo para abrir sua conta.")
            conta_corrente = ContaCorrente(nome=input('Nome: '),
                                           data_nascimento=input('Data nascimento dd/mm/aaaa: '),
                                           email=input('E-mail: '))
            conta_poupanca = ContaPoupanca(conta_corrente.nome, conta_corrente.data_nascimento, conta_corrente.email)
            print("\nConta corrente criada com Sucesso! ✅")
            conta_corrente.imprimir_dados()
            print("\nFoi criada também uma conta poupança integrada à sua conta! ✅")
            conta_poupanca.imprimir_dados()

            deposito = input("💬 Deseja realizar depósitos? (S - sim | N - não): ").strip().upper()
            if deposito.isalpha() and deposito in ['S', 'N']:
                if deposito == 'S':
                    print("\n🎉 Ótimo! Vamos começar o processo de depósitos na conta.")
                    conta_corrente.deposito(valor=float(input('Informe o valor do depósito: ')))
                else:
                    print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")

                transferencia = input("\n💬 Deseja realizar transferência para a poupança? (S - sim | N - não): ").strip().upper()
                if transferencia.isalpha() and transferencia in ['S', 'N']:
                    if transferencia == 'S':
                        conta_corrente.transfere(valor=float(input('Informe o valor da transferência: ')))
                    else:
                        print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")
                else:
                    print("❌\n Entrada inválida. Por favor, digite apenas 'S' para sim ou 'N' para não.\n")
                emprestimo = input("\n💬 Deseja realizar emprestimos? (S - sim | N - não): ").strip().upper()
                if emprestimo.isalpha() and emprestimo in ['S','N']:
                    if emprestimo == 'S':
                        print(f' 💰 Saldo disponivel para empréstimos: R$ {conta_corrente.creditoEmprestimo:.2f}')
                        conta_corrente.emprestimo(valor=float(input('Valor: ')), parcela=int(input('N° parc. a pagar: ')))
                    else:
                        print("\n👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")
                else:
                    print("❌\n Entrada inválida. Por favor, digite apenas 'S' para sim ou 'N' para não.\n")
            else:
                print("❌\n Entrada inválida. Por favor, digite apenas 'S' para sim ou 'N' para não.\n")
        else:
            print("👍 Sem problemas! Se mudar de ideia, estaremos aqui para ajudar.")
        break
    else:
        print("❌\n Entrada inválida. Por favor, digite apenas 'S' para sim ou 'N' para não.\n")
