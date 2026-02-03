import matplotlib.pyplot as plt
import numpy as np

# Pontos aproximados para reproduzir a curva do gráfico
tempo = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])
log_ufc = np.array([1.2, 1.3, 1.6, 3.0, 5.0, 7.2, 8.0, 8.2, 8.1, 7.8, 6.5, 5.0])

# Criação do gráfico
plt.figure(figsize=(8, 5))
plt.plot(tempo, log_ufc, color='black', linewidth=2)

# Linhas verticais delimitando as fases
plt.axvline(5, color='black', linewidth=1)
plt.axvline(11, color='black', linewidth=1)
plt.axvline(17, color='black', linewidth=1)

# Texto das fases
plt.text(2.2, 3, 'FASE LAG', rotation=90, va='center')
plt.text(7.5, 4.5, 'FASE\nEXPONENCIAL', rotation=90, va='center', ha='center')
plt.text(13.5, 5.5, 'FASE\nESTACIONÁRIA', rotation=90, va='center', ha='center')
plt.text(19.5, 4.5, 'FASE DE\nDECLÍNIO', rotation=90, va='center', ha='center')

# Rótulos dos eixos
plt.xlabel('tempo (horas)')
plt.ylabel('log UFC/g')

# Limites e grade
plt.xlim(1, 23)
plt.ylim(0, 9)
plt.grid(False)

plt.tight_layout()
plt.show()
