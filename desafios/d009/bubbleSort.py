import matplotlib.pyplot as plt
import numpy as np

# Dados extraídos da imagem
tamanhos = ['20k', '100k', '500k']

# Tempos (em segundos)
# [20k, 100k, 500k]
ordenada_classico = [4.684737, 209.07582, 10192.28988]
ordenada_otimizado = [0.001422, 0.006617, 0.027852]

aleatoria_classico = [4.592464, 165.795836, 8101.88904]
aleatoria_otimizado = [4.174295, 196.07257, 9235.029864]

inversa_classico = [1.171494, 66.347846, 4240.78402]
inversa_otimizado = [1.144495, 67.231682, 4285.21035]

x = np.arange(len(tamanhos))  # posições das legendas
width = 0.35  # largura das barras

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Função auxiliar para criar cada subplot
def criar_subplot(ax, dados_classico, dados_otimizado, titulo):
    rects1 = ax.bar(x - width/2, dados_classico, width, label='Bubble Sort Clássico', color='#4e79a7')
    rects2 = ax.bar(x + width/2, dados_otimizado, width, label='Bubble Sort Otimizado', color='#f28e2b')
    
    ax.set_ylabel('Tempo (segundos)')
    ax.set_title(titulo)
    ax.set_xticks(x)
    ax.set_xticklabels(tamanhos)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Adicionar rótulos acima das barras (opcional, pois os valores grandes podem poluir)
    # Mas ajuda a ver a diferença gritante no primeiro caso

# 1. Gráfico: Entrada Ordenada
criar_subplot(axs[0], ordenada_classico, ordenada_otimizado, 'Entrada Ordenada')
# Nota: Como a diferença é gigante aqui, vou setar escala log apenas neste se necessário, 
# mas o gráfico linear mostra o impacto visual da otimização (quase zero vs gigante).

# 2. Gráfico: Entrada Aleatória
criar_subplot(axs[1], aleatoria_classico, aleatoria_otimizado, 'Entrada Aleatória')

# 3. Gráfico: Entrada Inversamente Ordenada
criar_subplot(axs[2], inversa_classico, inversa_otimizado, 'Entrada Ordenada Inversamente')

plt.tight_layout()
plt.show()