# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
valor = float(input('Digite seu salário R$ '))
aumento = valor + (15 * valor / 100)
print(f'O seu novo salário com 15% de aumento é R${aumento}')
