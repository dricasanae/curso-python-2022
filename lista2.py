#Faça um Programa que peça dois números e imprima o maior deles
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O maior deles é", num1)
else:
    print("O maior deles é", num2)

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
num1 = float(input("Digite um valor: "))

if num1 > 0:
    print("Esse valor é positivo")
else:
    print("Esse valor é negativo")

#Faça um programa pra calcular o IMC e informar qual categoria pertence o IMC da pessoa.
peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em metros: "))
imc = peso/(altura**2)
print("O seu IMC é ", imc)
if imc < 18.5:
    print("Você esta abaixo do peso ideal")
elif 18.5 <= imc < 25:
    print("Você está no peso ideal")
elif 25 <= imc < 30:
    print("Você está com sobrepeso")
elif 30 <= imc < 40:
    print("Você está com obesidade")
else:
    print("Você está com obsesidade morbida")

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
letra = str(input("Digite seu sexo (M - masculino e F - feminino): "))
if letra == "M":
    print("Sexo masculino")
elif letra == "F":
    print("Sexo feminino")
else:
    print("Sexo inválido")

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input("Digite uma letra: "))
vogal = ["a","e","i", "o", "u"]
if letra in vogal:
    print("Esta letra é uma vogal")
else:
    print("Esta letra é uma consoante")

'''Faça um programa para a leitura de duas notas parciais de um aluno. O
programa deve calcular a média alcançada por aluno e apresentar:
a. A mensagem "Aprovado", se a média alcançada for maior ou igual a
sete;
b. A mensagem "Reprovado", se a média for menor do que sete;
c. A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2)/2
print("A media do aluno é ", media)
if media == 10:
    print("Aluno aprovado com Distinção")
elif media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno Reprovado")

#Faça um Programa que leia três números e mostre o maior deles.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 < num2 > num3:
    print(num2, "é o maior número.")
elif num2 < num1 > num3:
    print(num1,"é o maior número.")
else:
    print(num3, "é o maior número. ")

#Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 < num2 > num3 and num1 > num3:
    print(num2, "é o maior número.")
    print(num3, "é o menor número. ")
elif num1 < num2 > num3 and num3 > num1:
    print(num2, "é o maior número.")
    print(num1, "é o menor número. ")
elif num2 < num1 > num3 and num2 > num3:
    print(num1,"é o maior número.")
    print(num3, 'é o menor número.')
elif num2 < num1 > num3 and num3 > num2:
    print(num1,"é o maior número.")
    print(num2, 'é o menor número.')
elif num2 < num3 > num1 and num1 > num2:
    print(num3, "é o maior número. ")
    print(num2, 'é o menor número.')
else:
    print(num3, "é o maior número. ")
    print(num1, 'é o menor número.')

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
produto1 = float(input("Qual o preço do produto 1? "))
produto2 = float(input("Qual o preço do produto 2? "))
produto3 = float(input("Qual o preço do produto 3? "))

if produto2 > produto1 < produto3:
    print("Compre o produto 1.")
elif produto1 > produto2 < produto3:
    print("Compre o produto 2.")
else:
    print("Compre o produto 3.")

#Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
numbers = [num1, num2, num3]
numbers.sort(reverse = True)
print("A ordem descrecentes é ", numbers)

'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o
caso.'''

turno = str(input("Informe em qual turno você estuda (M- matutino, V- vespertino ou N - noturno): "))
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor inválido!")

'''Faça um Programa que peça um número inteiro e determine se ele é par ou
impar. Dica: utilize o operador módulo (resto da divisão - operador de módulo
% - se x % 2 == 0 então é par).'''

num1 = int(input("Digite um número inteiro: "))

if num1 % 2 == 0:
    print(num1, 'é par!')
else:
    print(num1,'é impar!')

'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
conceitos obedece à tabela abaixo:'''

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2)/2

if 9.0 < media <= 10:
    print("O conceito do aluno na disciplina é A")
elif 7.5 < media <= 9.0:
    print("O conceito do aluno na disciplina é B")
elif 6.0 < media <= 7.5:
    print("O conceito do aluno na disciplina é C")
elif 4.0 < media <= 6.0:
    print("O conceito do aluno na disciplina é D")
else:
    print("O conceito do aluno na disciplina é E")

'''Faça um Programa que leia um número e exiba o dia correspondente da
semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer
valor inválido.'''

semana = int(input("Digite um dia: "))
if semana == 1:
    print("O dia da semana é Domingo")
elif semana == 2:
    print("O dia da semana é Segunda-feira")
elif semana == 3:
    print("O dia da semana é Terça-feira")
elif semana == 4:
    print("O dia da semana é Quarta-feira")
elif semana == 5:
    print("O dia da semana é Quinta-feira")
elif semana == 6:
    print("O dia da semana é Sexta-feira")
elif semana == 7:
    print("O dia da semana é Sábado")
else:
    print("Valor inválido")

'''Faça um programa que permita o usuário escolher entre três opções de
bebidas e mostre na tela a bebida escolhida:'''
print("MENU")
print("1. AGUA")
print("2. REFRIGERANTE")
print("3. SUCO")
opcao = int(input("Digite o número correpondente a bebida que voce deseja: "))
if opcao == 1:
    print("A opção que voce escolheu foi água")
elif opcao == 2:
    print("A opção que voce escolheu foi refrigerante")
else:
    print("A opção que voce escolheu foi suco")
