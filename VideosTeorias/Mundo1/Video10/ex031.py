#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input('Digite a distancia da viagem em KM: '))
if km <= 200:
    total = km * 0.50
else:
    total = km * 0.45
print(f'O valor para sua viagem de {km}km ficou \033[4;32mR${total:.2f}\033[m')
