import sys
import os

from sympy.physics.units import years

# Adiciona o caminho absoluto do projeto ao PythonPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from datetime import datetime

from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Criando um objeto e testando


conta1 = ContaCorrente(nome='João', data_nascimento=datetime(year=1986, month=9, day=18), email='joao@hotmail.com')

print("\nDados Pessoais Conta Corrente:")
conta1.imprimir_dados()

print('\nRealizando operações:')
conta1.deposito(1000)
conta1.transfere(500)
conta1.saldo_conta_cp()
conta1.emprestimo(1000.00, 10)
conta1.chequeEsp()


# Criando um objeto e testando
conta2 = ContaPoupanca(nome='João', data_nascimento=datetime(year=1986, month=9, day=18), email='joao@hotmail.com')
print("\nDados Pessoais Conta Poupança:")
conta2.imprimir_dados()
print('\nRealizando operações:')
conta2.deposito(1000)
conta2.transfere(500)
conta2.calcular_rendimento(10)





