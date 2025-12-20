import matplotlib.pyplot as plt
import numpy as np

# Dados extraídos da imagem para Selection Sort
tamanhos = ['20k', '100k', '500k']

# Tempos (em segundos) - Selection Sort Clássico
# [20k, 100k, 500k]
sel_classico_ord = [0.383071, 10.331525, 1618.505994]
sel_classico_ale = [0.50827, 16.674911, 2595.16798]
sel_classico_inv = [0.451423, 14.12153, 2301.158436]

# Tempos (em segundos) - Selection Sort Estável
sel_estavel_ord = [0.276231, 12.574647, 1752.317941]
sel_estavel_ale = [0.403284, 16.740321, 2457.641692]
sel_estavel_inv = [0.515791, 16.517403, 2536.014792]

x = np.arange(len(tamanhos))  # posições das legendas
width = 0.35  # largura das barras

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Função auxiliar para manter o padrão visual
def criar_subplot(ax, dados_classico, dados_estavel, titulo):
    # Usando cores diferentes do Bubble Sort (verde e roxo) para diferenciar no relatório
    rects1 = ax.bar(x - width/2, dados_classico, width, label='Selection Clássico', color='#59a14f')
    rects2 = ax.bar(x + width/2, dados_estavel, width, label='Selection Estável', color='#b07aa1')
    
    ax.set_ylabel('Tempo (segundos)')
    ax.set_title(titulo)
    ax.set_xticks(x)
    ax.set_xticklabels(tamanhos)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)

# 1. Gráfico: Entrada Ordenada
criar_subplot(axs[0], sel_classico_ord, sel_estavel_ord, 'Entrada Ordenada')

# 2. Gráfico: Entrada Aleatória
criar_subplot(axs[1], sel_classico_ale, sel_estavel_ale, 'Entrada Aleatória')

# 3. Gráfico: Entrada Inversamente Ordenada
criar_subplot(axs[2], sel_classico_inv, sel_estavel_inv, 'Entrada Ordenada Inversamente')

plt.suptitle('Comparativo de Performance: Selection Sort (Clássico vs Estável)', fontsize=16)
plt.tight_layout()
plt.show()