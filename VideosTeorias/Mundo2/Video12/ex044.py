#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
while True:
    prod = float(input("Digite o valor do produto: "))
    menu = int(input("Condição de pagamento: \n 1 - à vista dinheiro/cheque \n 2 - à vista no cartão \n 3 - em até 2x no cartão: preço formal \n 4 - 3x ou mais no cartão \n 5 - Finalizar Programa \nDigite o desejado: "))
    if menu == 1:
        valor = prod - (prod * 10/100)
        print(f"O Valor do produto é {prod:.2f}, mas com desconto final ficou R${valor:.2f}")
        
    elif menu == 2:
        valor = prod - (prod * 5/100)
        print(f"O Valor do produto é {prod:.2f}, mas com desconto final ficou R${valor:.2f}")
        
    elif menu == 3:
        valor = prod
        parcela = valor / 2
        print(f"Sua compra será parcelada em 2x de {parcela:.2f}!")
        print(f"O Valor final do produto é R${prod}, sem juros!")
        
    elif menu == 4:
        valor = prod + (prod * 20/100)
        totalparc = int(input("Quantas parcelas: "))
        parcela = valor / totalparc
        print(f"Sua compra será parcelada em {totalparc}x de R${parcela:.2f} com juros!")
        print(f"O Valor do produto é {prod:.2f}, mas com juros final ficou R${valor:.2f}!")

    elif menu == 5:
        print("Saindo do programa...")
        break
       
    else:
        print("Opção inválida!")

    print("\n" + "-"*30 + "\n")  # Separador visual
        
        
