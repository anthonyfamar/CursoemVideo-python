#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.   
# ex:Digite um número:6.127 o número tem a parte inteiro 6.
from math import trunc
num = float(input('Digite um número do tipo real: '))
print(f'o número inteiro é: {trunc(num)}')






#ou desse jeito:
#  num = float(input('Digite um número do tipo real: '))
#  trunc_num = trunc(num)
#  print(f'o número inteiro é: {trunc_num}')
