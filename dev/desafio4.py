# string [e] texto

produto=input("digite o nome do produto  ")
qtde=int(input("digite a qtde de produto  "))
preco=float(input("digite o valor do produto  "))
total=qtde*preco
print('o valor total:', total) # concatenar
print(f'o produto {produto} tem o valor total de {total}')   #interpolar

# Estrutura condicional
# se o valor total for maio que 1000 entao da um desconto de 10
# >  <  ==
if total >= 1000:
    print("o valor total e maior ou igual a 1000 ") 


