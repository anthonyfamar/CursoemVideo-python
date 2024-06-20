# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
a1 = 'Anthony'
a2 = 'Oda'
a3 = 'Bruno'
a4 = 'Gustavo'
print(f'Os alunos que falta apresentar são os seguintes: {a1, a2, a3, a4}')
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print(f'A ordem de apresentação será: {alunos}')