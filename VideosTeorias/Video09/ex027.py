#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza (primeiro = Ana; último = Souza).
nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print(f'Seu primeiro nome é {separado[0]}')
print(f'Seu último nome é {separado[-1]}')


#obs: o [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante.