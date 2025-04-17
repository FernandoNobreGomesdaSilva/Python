import sys
import os
# Adiciona o caminho absoluto do projeto ao PythonPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Criando um objeto e testando
conta1 = ContaCorrente("João Silva", "18/09/1978", "joao.silva@example.com")

print("\nDados Pessoais Conta Corrente:")
conta1.imprimir_dados()

print('\nRealizando operações:')
conta1.deposito(1000)
conta1.transfere(500)
conta1.conta_poupanca()
conta1.emprestimo(1000.00, 10)
conta1.chequeEsp()


# Criando um objeto e testando
conta2 = ContaPoupanca("João Silva", "18/09/1978", "joao.silva@example.com")
print("\nDados Pessoais Conta Poupança:")
conta2.imprimir_dados()
print('\nRealizando operações:')
conta2.deposito(1000)
conta2.transfere(500)
conta2.calcularJuros(10)





