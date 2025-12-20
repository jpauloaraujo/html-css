import matplotlib.pyplot as plt
import numpy as np

# Dados extraídos (Quick Sort)
tamanhos = ['20k', '100k', '500k']

# NOTA: Para os casos de StackOverflowError, usamos 0 para o gráfico,
# mas vamos adicionar uma anotação visual explicativa.

# 1. Quick Sort (Versão do Slide)
# Falha nos casos ordenados e inversos devido à escolha do pivô
qs_slide_ord = [0, 0, 0] # StackOverflowError
qs_slide_ale = [0.001124, 0.006386, 0.035673]
qs_slide_inv = [0, 0, 0] # StackOverflowError

# 2. Quick Sort + Shuffle (Resolve o pior caso)
qs_shuffle_ord = [0.00096, 0.004044, 0.020606]
qs_shuffle_ale = [0.001531, 0.008502, 0.04632]
qs_shuffle_inv = [0.000961, 0.004258, 0.021089]

# 3. Quick Sort (Versão do Java - Dual Pivot / Otimizado)
qs_java_ord = [0.000348, 0.000456, 0.000172]
qs_java_ale = [0.001383, 0.00476, 0.025643]
qs_java_inv = [0.000588, 0.00048, 0.000312]

x = np.arange(len(tamanhos))
width = 0.25  # Barras mais finas para caberem 3

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

def criar_subplot(ax, dados_slide, dados_shuffle, dados_java, titulo):
    # Barras
    rects1 = ax.bar(x - width, dados_slide, width, label='QS Slide (Ingênuo)', color='#e15759') # Vermelho para indicar perigo/erro
    rects2 = ax.bar(x, dados_shuffle, width, label='QS + Shuffle', color='#4e79a7')
    rects3 = ax.bar(x + width, dados_java, width, label='QS Java', color='#76b7b2')
    
    ax.set_ylabel('Tempo (segundos)')
    ax.set_title(titulo)
    ax.set_xticks(x)
    ax.set_xticklabels(tamanhos)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Lógica para anotar o StackOverflow
    # Se o valor for 0 e for a série do Slide, escrevemos o erro
    if sum(dados_slide) == 0:
        for i in range(len(tamanhos)):
            ax.text(x[i] - width, 0.001, 'Stack\nOverflow', ha='center', va='bottom', fontsize=9, color='red', rotation=90)

# Gerar os 3 gráficos
criar_subplot(axs[0], qs_slide_ord, qs_shuffle_ord, qs_java_ord, 'Entrada Ordenada')
criar_subplot(axs[1], qs_slide_ale, qs_shuffle_ale, qs_java_ale, 'Entrada Aleatória')
criar_subplot(axs[2], qs_slide_inv, qs_shuffle_inv, qs_java_inv, 'Entrada Ordenada Inversamente')

plt.suptitle('Comparativo de Performance: Quick Sort e Variações', fontsize=16)
plt.tight_layout()
plt.show()