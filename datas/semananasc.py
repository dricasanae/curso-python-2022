# 1 - Crie um programa que receba o dia, mês e ano de 
# nascimento de uma pessoa. Use a biblioteca datatime 
# pra verificar o dia da semana que a pessoa nasceu. 

import datetime
import locale
locale.setlocale(locale.LC_ALL, "pt_br")

ano = int(input("Digite seu ano de nascimento: "))
mes = int(input("Digite seu mês de nascimento em formato numérico: "))
dia = int(input("Digite seu dia de nascimento: "))
nasc = datetime.datetime(ano, mes, dia)
print("Você nasceu em: ", nasc)
print("No dia da semana:")
print(nasc.strftime("%A"))