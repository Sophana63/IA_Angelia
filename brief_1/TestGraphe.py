import numpy as np
import matplotlib.pyplot as plt

x = range(2015, 2022) # donner les deux extrêmités sur l'axe des abscisses
y1 = [0.5957923803229163, 0.6041403681313708, 0.6249721812114458, 0.6345097476225332, 0.6497241034685495, 0.6571294754968777, 0.6715305046967041] # donner les différentes données pour constituer la courbe
y2 = [0.08505499952790083, 0.09510230082107737, 0.10051705935888398, 0.10821225310899783, 0.11116824556983344, 0.11227856066585337, 0.1304163031364433]
y3 = [0.09665847457627105, 0.10683086419753086, 0.09937358490566035, 0.0862046511627907, 0.07542666666666667, 0, 0]

# nommer les différentes courbes
plt.plot(x, y1, label='Danceability')
plt.plot(x, y2, label='Speechiness')
plt.plot(x, y3, label='Duration_ms')
plt.legend()
plt.title('Test')
plt.grid(True)
plt.show() #affiche la figure à l'écran