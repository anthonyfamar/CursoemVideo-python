#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))
#""se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo"
if a + b > c and b + c > a and a + c > b:
    print('Pode formar um triângulo!')
else:
    print('Não pode formar um triângulo!') 