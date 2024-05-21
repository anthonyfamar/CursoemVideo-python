# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
valor = float(input('Digite seu salário: '))
aumento = (15 * valor) / 100
salario = valor + aumento
print(f'O seu novo salário é R${salario}')
