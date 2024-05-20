# isalnum – Verifique se todos os caracteres no texto são alfanuméricos(possui letras ou números)
# isascii – Verifique se a sequência é composta por todos os caracteres ASCII ou se a sequência estiver vazia também retornara true
# isdecimal – Verifique se todos os caracteres no objeto unicode são decimais
# isdigit – Verifique se todos os caracteres no texto são dígitos

# isidentifier – Verifique se a sequência é um identificador válido :: O método isidentifier () retornará True 
# se a string for um identificador válido, caso contrário, False. Uma sequência é considerada um identificador válido se contiver apenas letras alfanuméricas (a-z) e (0-9) ou sublinhados (_). Um identificador válido não pode começar com um número ou conter espaços.

# isalpha – Verifique se todos os caracteres no texto são apenas letras
# isnumeric – Verifique se todos os caracteres no texto são apenas numéricos
# isprintable – Verifique se todos os caracteres no texto são imprimíveis
# isspace – Verifique se todos os caracteres no texto são espaços em branco
# istitle – Verifique se cada palavra começa com uma letra maiúscula
# isupper – Verifique se todos os caracteres do texto estão em maiúsculas
# islower – Verifique se todos os caracteres do texto estão em minúsculas

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e  todas as informações possíveis sobre ele.

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(algo))
print('Só tem espaços em brancos? ', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico(letras e números)?', algo.isalnum())
print('Está tudo em maiúsculo?', algo.isupper())
print('Está tudo em minúsculo?', algo.islower())
print('Está capitalizada?', algo.istitle())