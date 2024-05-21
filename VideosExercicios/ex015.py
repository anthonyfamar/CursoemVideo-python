#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantidade de KM percorrido: '))
dia = int(input('Quantidade de dias alugado: '))
preco = 60 * dia + 0.15 * km
print(f'O preço a pagar pelo carro é R${preco:.2f}')