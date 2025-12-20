import matplotlib.pyplot as plt
import numpy as np

# --- DADOS: BUSCAS LINEARES ---
tamanhos = ['20k', '100k', '500k']
x = np.arange(len(tamanhos))
width = 0.25

# 1. Busca Linear Iterativa
# [20k, 100k, 500k]
lin_iter_melhor = [0.00000086, 0.000000587, 0.000000693]
lin_iter_medio  = [0.00015214, 0.000192187, 0.001249453]
lin_iter_pior   = [0.00015382, 0.000336893, 0.002651133]

# 2. Busca Linear Recursiva
# Nota: 0 indica StackOverflowError (exceto onde há dados válidos)
lin_rec_melhor = [0.000000627, 0.000000687, 0.000001333] # Funciona no melhor caso (profundidade 1)
lin_rec_medio  = [0.000083253, 0, 0] # Falha em 100k e 500k
lin_rec_pior   = [0, 0, 0]           # Falha em todos (profundidade N)

# 3. Busca Linear Duas Pontas
lin_duas_melhor = [0.0000009, 0.000000607, 0.00000058]
lin_duas_medio  = [0.000231853, 0.000743953, 0.00321088]
lin_duas_pior   = [0.000389493, 0.000604547, 0.003414993]

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

def plot_linear(ax, dados_iter, dados_rec, dados_duas, titulo):
    rects1 = ax.bar(x - width, dados_iter, width, label='Linear Iterativa', color='#4e79a7')
    rects2 = ax.bar(x, dados_rec, width, label='Linear Recursiva', color='#e15759') # Vermelho = perigo/erro
    rects3 = ax.bar(x + width, dados_duas, width, label='Linear 2 Pontas', color='#f28e2b')
    
    ax.set_ylabel('Tempo (segundos)')
    ax.set_title(titulo)
    ax.set_xticks(x)
    ax.set_xticklabels(tamanhos)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Anotar StackOverflow onde o valor for 0 e for Recursiva
    for i in range(len(dados_rec)):
        if dados_rec[i] == 0:
            ax.text(x[i], 0.0001, 'Stack\nOverflow', ha='center', va='bottom', fontsize=8, color='red', rotation=90)

plot_linear(axs[0], lin_iter_melhor, lin_rec_melhor, lin_duas_melhor, 'Melhor Caso')
plot_linear(axs[1], lin_iter_medio, lin_rec_medio, lin_duas_medio, 'Caso Médio')
plot_linear(axs[2], lin_iter_pior, lin_rec_pior, lin_duas_pior, 'Pior Caso')

plt.suptitle('Comparativo: Buscas Lineares (Iterativa, Recursiva e Duas Pontas)', fontsize=16)
plt.tight_layout()
plt.show()