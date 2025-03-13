#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
atual = int(input("Digite o ano atual: "))
nascimento = int(input("Digite seu ano de nascimento: "))
idade = atual - nascimento

if idade <= 9:
    print(f"Sua categoria é MIRIM!")
elif 9 < idade <=14 :
    print(f"Sua categoria é INFANTIL!")
elif 14 < idade <=19:
    print(f"Sua categoria é JÚNIOR!")
elif 19 < idade <= 25:
    print("Sua categoria é SÊNIOR!")
else:
    print("Sua categoria é MASTER!")