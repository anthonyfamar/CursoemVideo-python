#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
atual = int(input("Digite o ano atual: "))
nascimento = int(input("Digite seu ano de nascimento: "))
idade = atual - nascimento
if idade < 18:
    falta = 18 - idade
    print(f"Ainda não está na hora de se alistar, faltam {falta} anos para se alistar!")
elif idade > 18:
    passou = idade - 18
    print(f"Já se passou {passou} ano(s) do prazo, corra para se alistar!")
else:
    print("Você está no tempo certo para se alistar!")