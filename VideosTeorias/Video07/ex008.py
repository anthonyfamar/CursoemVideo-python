# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n1 = float(input('Digite um valor em metros: '))
cm = n1 * 100
mm = n1 * 1000
print(f'O valor convertido é: \n{cm:.0f} centímetros \n{mm:.0f} milímetros')