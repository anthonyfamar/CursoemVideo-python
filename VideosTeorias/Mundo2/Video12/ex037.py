#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro:'))
print('Selecione a base que deseja converter: ')
menu = int(input('1-Binário \n2-Octal \n3-Hexadecimal\n'))
if menu == 1:
    converte = bin(num)
    print(f'O número convertido para a base binária é {converte[2:]}')
elif menu == 2:
    converte = oct(num)
    print(f'O número convertido para a base octal é {converte[2:]}')
elif menu == 3:
    converte = hex(num)
    print(f'O número convertido para a base hexadecimal é {converte[2:]}')
else:
    print('Escolha Inválida!')

