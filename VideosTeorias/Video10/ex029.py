#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Digite a velocidade que passou pelo radar: '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Execeu o limite de 80km/h da via, será multado em R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')