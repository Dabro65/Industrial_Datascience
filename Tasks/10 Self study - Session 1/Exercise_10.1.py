import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)         # Array mit 100 Werten von 0 bis 10
y = np.sin(t)                       # Für jeden Wert t wird der Sinuswert berechnet

plt.plot(t, y)                      # Die Werte von t und y werden geplottet
plt.show()                          # Das Diagramm wird angezeigt