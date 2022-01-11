# Adicione em uma lista e imprimanpo final.
# Adicionar  o endereço, adicionar  o peso
#- Verifiquem se a pessoa é maior de idade: MAIOR DE IDADE: Você é maior de idade. MENOR DE IDADE: Você é menor de idade. 
n = int(input("Quantas pessoas deseja cadastrar: "))
lista_pessoas = []
for indice in range(n):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    ender = input("Digite o seu endereço: ")
    peso = float(input("Digite o seu peso: "))
    nova_pessoa = [nome, idade, ender, peso]
    lista_pessoas.append(nova_pessoa)

for pessoa in lista_pessoas:
    print(f"Bem-vin@ {pessoa[0]}, você tem {pessoa[1]} anos. Você mora no endereço {pessoa[2]}. E pesa {pessoa[3]} kg!")
    if pessoa[1] >= 18:
        print("Você é maior de idade")
    else:
        print('Você é menor de idade')