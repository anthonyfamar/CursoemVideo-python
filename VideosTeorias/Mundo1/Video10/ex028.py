#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
num = randint(0,5)
n = int(input('Digite um número inteiro entre 0 e 5 que você acha que o computador irá escolher: '))
if num == n:
    print('\033[37;42mParabéns, você venceu!\033[m')
else:
    print(f'Você \033[41mPERDEU\033[m, o número escolhido foi {num}, tente novamente!')
