#Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e 
# continue pedindo até que o usuário informe um valor válido.
while  True :
    nota = float(input("Digite um valor entre 0 e 10: "))
    if (0 <= nota <= 10) :
        print("Parabéns, a nota esta dentro do intervalo 0 e 10! ")
        break
    else:
        print("Continue tentando. O valor informado nao esta entre 0 e 10.")