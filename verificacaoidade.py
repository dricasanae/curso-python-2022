#Crie um programa que peça o ano de nascimento e calcule a idade e verifique SE a pessoa é maior de idade.
#Entrada
ano = int(input("Digite seu ano de nascimento: "))
idade = 2021 - ano

#Processamento
print(idade, "anos")
if idade >= 18:
     print("Maior de idade")
else:
    print("Menor de idade")