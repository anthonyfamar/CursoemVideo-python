#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
r = n1 ** 2
print(f'O dobro é {d:=^8} \nO triplo é {t:=^8} \nA raiz quadrada é {r:=^8}')
