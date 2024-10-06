#calcular descontos
n1 = float(input("Qual o valor a ser descontado? \n"))
n2 = float(input("Informe o desconto \n"))
desconto = n1 - (n1*n2/100)
print("O desconto é de ",desconto)