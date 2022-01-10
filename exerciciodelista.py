'''Crie um programa que tenha uma lista de 5 frutas, e depois adicione uma nova fruta no final da lista. 
Depois remova o primeiro elemento da lista e por fim, altere o valor do item 2 pra "banana"'''

frutas = ["laranja","maça", "uva", "pera", "melão"]
frutas.append("kiwi")
frutas.pop(0)
frutas[1] = "banana"

print(frutas)

'''Crie uma lista com os dados de 4 pessoas (nome, idade, sexo, ano_nascimento).
Dica:  Usar lista de lista'''
dados = []
pessoa1 = ['Adryelle', 24, "Feminino", 1997]
dados.append(pessoa1)
pessoa2 = ["Brunna", 28, "Feminino", 1993]
dados.append(pessoa2)
pessoa3 = ["Fernando", 26, "Masculino", 1995]
dados.append(pessoa3)
pessoa4 = ["Carlos", 61, "Masculino", 1960]
dados.append(pessoa4)

print(dados)


