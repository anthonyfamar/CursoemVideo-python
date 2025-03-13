#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
print('=-'*20)
print('Analisador de triângulos')
print('-='*20)
a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))
#""se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo"
if a + b > c and b + c > a and a + c > b:
    print('Pode formar um triângulo ', end='')
    if a == b == c:
        print("EQUILÁTERO!")
    elif a != b != c != a:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print('Não pode formar um triângulo!') 