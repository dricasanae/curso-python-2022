'''Crie um gráfico linha em Python para mostrar 
a relação da quantidade de litros de agua ingerido por calorias. '''
import numpy as np
import matplotlib.pyplot as plt

y = np.array([4,5,6,4,7,8,7])
x = np.array([140,120,122,150,125,180,165])

plt.plot(y,x)

plt.xlabel("Calorias")
plt.ylabel("Quantidade de litros de água")

plt.show()