#2 - Faça um programa que imprima na tela 
# apenas os números ímpares entre 1 e 50.

num = 1
while num >= 1 and num <= 50:
    if (num % 2) == 0:
       num += 1
       continue
    else:
        print(num)
    num += 1