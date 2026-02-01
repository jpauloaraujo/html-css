import numpy as np
import matplotlib.pyplot as plt

# Configuração do gráfico
plt.figure(figsize=(6, 6))

# 1. Desenhar a Curva de Nível: x^2 + y^2 = 2
# Usamos parametrização para um círculo perfeito: x = r*cos(t), y = r*sin(t)
r = np.sqrt(2)
t = np.linspace(0, 2*np.pi, 100)
x = r * np.cos(t)
y = r * np.sin(t)

plt.plot(x, y, label=r'Curva de Nível: $x^2 + y^2 = 2$', color='blue', linewidth=2)

# 2. Plotar o ponto (1, 1)
plt.plot(1, 1, 'go', label='Ponto (1, 1)')

# 3. Plotar o vetor gradiente (1, 1) partindo do ponto (1, 1)
plt.quiver(1, 1, 1, 1, angles='xy', scale_units='xy', scale=1, color='red', label=r'Gradiente $\nabla f = (1, 1)$')

# Ajustes visuais para melhor compreensão
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower right')
plt.title(r'Curva de Nível de $f(x,y) = \ln(x^2+y^2)$')
plt.gca().set_aspect('equal', adjustable='box') # Essencial para o círculo não parecer uma elipse

plt.show()