# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.  Considere US$1,00 = R$3,27

valor = float(input('Digite o valor que possui R$'))
dolar = valor / 3.27
print(f'Com R${valor}, vc poderá comprar US$ {dolar:.2f}')