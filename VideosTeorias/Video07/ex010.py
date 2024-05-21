# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.  Considere US$1,00 = R$3,27

valor = float(input('Digite o valor que possui: '))
dolar = valor * 3.27
print(f'Vc poderá comprar US$ {dolar}')