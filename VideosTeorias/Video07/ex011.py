# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
b = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
a = b * h
print(f'A área total da parede é: {a} m\u00B2')
tinta = a / 2
print(f'A quantidade de tinta necessária para pintar é: {tinta} litros')