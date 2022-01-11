#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
while  True :
    nome = input("Digite nome do usuario: ")
    senha = input("Digite a sua senha: ")
    if nome != senha :
        print("Parabéns, usuário e senha cadastrado ")
        break
    else:
        print("Erro! Favor tente novamente!")