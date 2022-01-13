#Crie um programa em Python que 
# calcule as raizes reais de uma equação do segundo grau.
import equacao2grau

a = float(input("Digite o valor do coeficiente a: "))
b = float(input("Digite o valor do coeficiente b: "))
c = float(input("Digite o valor do coeficiente c: "))
ver = equacao2grau.delta(a,b,c)
if ver >= 0:
    print("A sua equação de segundo grau é: ", a,"x^2+",b,"x+",c)
    print("O valor de x1 é:", equacao2grau.raiz(a,b,ver))
    print("O valor de x2 é:", equacao2grau.raiz2(a,b,ver))
else:
    print("Não existe raizes reais para essa equação!")