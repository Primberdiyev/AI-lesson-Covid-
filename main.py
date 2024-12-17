import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

y = np.sin(x)

plt.plot(x, y, color='blue', linewidth=2, label='Sinus(x)')

plt.title("Sinus Funksiyasining Grafiki")
plt.xlabel("X qiymatlari")
plt.ylabel("Y qiymatlari")

plt.grid(True)


plt.legend()

plt.show()





import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(0, 10, 50) 
y = np.random.uniform(0, 10, 50) 

plt.scatter(x, y, color='blue', edgecolors='purple', s=80, label="Nuqtalar")

plt.title("Tasodifiy Nuqtalar Scatter Grafiki")
plt.xlabel("X qiymatlari")
plt.ylabel("Y qiymatlari")

plt.grid(True)

plt.legend()

plt.show()