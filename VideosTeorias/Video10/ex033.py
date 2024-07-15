#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite o último número: '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')