#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número: '))
resto = num % 2
if resto==0:
    print('O número que você escolheu é par!')
else:
    print('O número que você escolheu é impar!')