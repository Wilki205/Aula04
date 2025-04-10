soma=0
num = int(input("Digite quantos numeros: "))
for x in range(num):
    n = float(input("Digite um numero: "))
    soma=soma+n
media = soma/num
print (f"a media é: {media}")