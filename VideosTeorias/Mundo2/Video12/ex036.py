#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('\033[1;32m-=\033[m'*10)
print('   \033[1;32mBanco THONYN \033[m')
print('\033[1;32m-=\033[m'*10)
print('Seja bem vindo!')
casa = float(input('Qual o valor da casa que deseja comprar? R$'))
salario = float(input('Certo, e qual seria o valor do seu salário? R$'))
tempo = int(input('E por último, em quantos anos deseja quitar ela? '))
prestação = casa/(tempo*12)
         
if prestação > 0.30 * salario:
    print('Financimento negado, pois o valor passou 30% do seu salário!')
else:
    print('Financiamento aprovado! PARABÉNS!')