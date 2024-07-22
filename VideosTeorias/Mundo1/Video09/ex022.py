#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome completo tudo em maiúscula é: {nome.upper()}')
print(f'Seu nome completo tudo em minúsculo é: {nome.lower()}')
print(f'Quantidade de letras: {len(nome) - nome.count(' ')}')
dividido = nome.split()
print(f'O primeiro nome tem {len(dividido[0])} letras')
#ou
print(f'Seu primeiro nome tem {nome.find(' ')} letras')