import numpy as np
import matplotlib.pyplot as plt

# Erstellt 1000 gleichmäßig verteilte Werte von 0 bis 2 Pi.
t = np.linspace(0, 2 * np.pi, 1000)

# Berechnet die x-Koordinaten der Herzfunktion.
x = 16 * np.sin(t) ** 3

# Berechnet die y-Koordinaten der Herzfunktion.
y = (
    13 * np.cos(t)
    - 5 * np.cos(2 * t)
    - 2 * np.cos(3 * t)
    - np.cos(4 * t)
)

# Stellt die berechneten Koordinaten als Linie dar.
plt.plot(x, y)

# Verwendet für beide Achsen denselben Maßstab.
plt.axis("equal")

# Zeigt das Diagramm an.
plt.show()