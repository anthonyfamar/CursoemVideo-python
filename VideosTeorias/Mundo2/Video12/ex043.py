#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
peso = float(input("Digite seu peso em kg: "))
alt = float(input("Digite sua altura em metros:"))
imc = peso/(alt ** 2)

print(f"Seu IMC é {imc:.2f}kg/m², está ", end='')
if imc < 18.5:
    print("ABAIXO DO PESO!")
elif 18.5 <= imc < 25:
    print("no PESO IDEAL!")
elif 25 <= imc < 30:
    print("com SOBREPESO!")
elif 30 <= imc < 40:
    print("com OBESIDADE!")
elif imc >= 40:
    print("grave, OBESIDADE MÓRBIDA!")  