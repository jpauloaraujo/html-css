import numpy as np
import matplotlib.pyplot as plt

# Configuração do gráfico
plt.figure(figsize=(6, 6))

# 1. Curva de Nível: x^2 + y^2 = 4 (Círculo raio 2)
t = np.linspace(0, 2*np.pi, 100)
x_circle = 2 * np.cos(t)
y_circle = 2 * np.sin(t)
plt.plot(x_circle, y_circle, label=r'Curva $x^2 + y^2 = 4$', color='blue')

# Ponto dado: (sqrt(2), sqrt(2)) -> Aprox (1.41, 1.41)
p_val = np.sqrt(2)
plt.plot(p_val, p_val, 'go', label=r'Ponto $(\sqrt{2}, \sqrt{2})$')

# 2. Gradiente: (2*sqrt(2), 2*sqrt(2)) -> Aprox (2.82, 2.82)
# Vamos escalar o vetor visualmente para ele não ficar enorme no gráfico, mantendo a direção.
# O vetor real tem magnitude 4. Vamos desenhar com escala menor mas indicando que é o gradiente.
plt.quiver(p_val, p_val, 2*p_val, 2*p_val, angles='xy', scale_units='xy', scale=1, color='red', label=r'Gradiente $\nabla f$')

# 3. Reta Tangente: y = -x + 2*sqrt(2)
x_line = np.linspace(-1, 4, 100)
y_line = -x_line + 2*p_val
plt.plot(x_line, y_line, '--', color='green', label='Reta Tangente')

# Ajustes visuais
plt.xlim(-3, 5)
plt.ylim(-3, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower left')
plt.title(r'Exercício 25: $x^2+y^2=4$')
plt.gca().set_aspect('equal', adjustable='box')

plt.show()