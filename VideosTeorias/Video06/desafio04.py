# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e  todas as informações possíveis sobre ele.

algo = input('Digite algo: ')
print(algo, 'É do tipo primitivo', type(algo))
print(algo,'Possui apenas números?', algo.isnumeric())
print(algo,'Possui apenas letras?', algo.isalpha())
print(algo,'Possui letras ou números?', algo.isalnum())
print(algo,'Possui números de 0 a 9?', algo.isdecimal())
print(algo,'Possui todos as palavras em minúsculo?', algo.islower())
print(algo,'Possui espaços apenas espaços em branco?', algo.isspace())
print(algo,'Possui apenas letras maiúsculas?', algo.isupper())
print(algo,'Possui a primeira palavra maiúscula e o restante minúsculas?',algo.istitle())