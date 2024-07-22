#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
a1 = 'Anthony'
a2 = 'Oda'
a3 = 'Bruno'
a4 = 'Gustavo'
a5 = 'David'
print(f' Alunos: {a1, a2, a3, a4, a5}')
alunos = choice([a1, a2, a3, a4, a5])
print(f'O aluno que irá apagar o quadro é o \033[1;37;41m{alunos}\033[m')