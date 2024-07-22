#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número: '))
resto = num % 2
if resto==0:
    print('\033[1;34mO número que você escolheu é par!\033[m')
else:
    print('\033[1;33mO número que você escolheu é impar!\033[m')