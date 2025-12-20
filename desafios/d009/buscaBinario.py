import matplotlib.pyplot as plt
import numpy as np

# --- DADOS: BUSCAS BINÁRIAS ---
tamanhos = ['20k', '100k', '500k']
x = np.arange(len(tamanhos))
width = 0.35

# 1. Busca Binária Iterativa
bin_iter_melhor = [0.00000026, 0.000002513, 0.000000286]
bin_iter_medio  = [0.000003007, 0.000000434, 0.000003167]
bin_iter_pior   = [0.000001713, 0.000001853, 0.000001947]

# 2. Busca Binária Recursiva
bin_rec_melhor = [0.000000356, 0.000005247, 0.000000334]
bin_rec_medio  = [0.000002687, 0.000005973, 0.000003567]
bin_rec_pior   = [0.000004293, 0.000002173, 0.000003433]

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

def plot_binaria(ax, dados_iter, dados_rec, titulo):
    rects1 = ax.bar(x - width/2, dados_iter, width, label='Binária Iterativa', color='#59a14f')
    rects2 = ax.bar(x + width/2, dados_rec, width, label='Binária Recursiva', color='#b07aa1')
    
    ax.set_ylabel('Tempo (segundos)')
    ax.set_title(titulo)
    ax.set_xticks(x)
    ax.set_xticklabels(tamanhos)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)

plot_binaria(axs[0], bin_iter_melhor, bin_rec_melhor, 'Melhor Caso')
plot_binaria(axs[1], bin_iter_medio, bin_rec_medio, 'Caso Médio')
plot_binaria(axs[2], bin_iter_pior, bin_rec_pior, 'Pior Caso')

plt.suptitle('Comparativo: Buscas Binárias (Iterativa vs Recursiva)', fontsize=16)
plt.tight_layout()
plt.show()