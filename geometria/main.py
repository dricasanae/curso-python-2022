import areas
opcao = int(input("Digite qual opção você quer calcular a área (1- Cículo ou 2 - Quadrado): "))

if opcao == 1:
    raio = float(input("Digite o raio do círculo: "))
    print("A area do cículo é ", areas.area_circulo(raio) )
elif opcao == 2:
    lado = float(input("Digite o lado do quadrado: "))
    print("A área do quadrado é ", areas.area_quadrado(lado))
else:
    print("Opção invalida")