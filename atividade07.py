dentro = 0
fora = 0
for x in range(10):
    num = int(input("digite um numero: "))
    if num >=10 or num <=20:
      fora = fora=1
dentro = 5-fora
print (f"{dentro} numeros dentro\n e {fora} numeros fora")
