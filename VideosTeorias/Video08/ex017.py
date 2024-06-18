# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Digite o cateto oposto do triângulo: '))
ca = float(input('Digite o cateto adjacente do triângulo: '))
h = hypot(co, ca)
print(f'o comprimento da hipotenusa é {h:.2f}')
#ou
print(f'o comprimento da hipotenusa é {hypot(co,ca):.2f}')

