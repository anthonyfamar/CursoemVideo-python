#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import sin, cos, tan, radians, degrees
ang = float(input('Digite um ângulo: '))
ang_conv = radians(ang)
sen = sin(ang_conv)
coss = cos(ang_conv)
tang = tan(ang_conv)
print(f'o seno é {sen:.2f}, o cosseno é {coss:.2f} e a tangente é {tang:.2f}')