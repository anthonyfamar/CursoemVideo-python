#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;4;32mO ano {ano} É BISSEXTO!\033[m')
else:
    print(f'\033[4;1;31mO ano {ano} NÃO É BISSEXTO!\033[m')