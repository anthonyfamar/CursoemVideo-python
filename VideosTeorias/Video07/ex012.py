# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preco = float(input('Digite o preço do produto R$ '))
desc = preco - (5 * preco / 100)
print(f'O valor final com desconto é R${desc:.2f}')