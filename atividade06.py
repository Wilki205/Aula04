neg = 0
for n in range(10):
        num = int(input("Digite um numero: "))
        if num < 0:
         neg = neg + 1
print(f"{neg} numeros negativos encontrados!")