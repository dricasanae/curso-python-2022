'''Crie um gráfico pizza em Python para mostrar 
por dia da semana o número de frutas que uma pessoa comprou:'''
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Segunda", "Terça","Quarta", "Quinta"]

plt.pie(y, labels = mylabels)
plt.show()

