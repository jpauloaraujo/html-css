#include <stdio.h>

// Estrutura para armazenar o tempo decomposto
struct Tempo {
    int horas;
    int minutos;
    int segundos;
};

// Função que converte o total de segundos em uma struct Tempo
struct Tempo converterSegundos(int totalSegundos) {
    struct Tempo t;

    // Cálculo das horas, minutos e segundos restantes
    t.horas = totalSegundos / 3600;
    t.minutos = (totalSegundos % 3600) / 60;
    t.segundos = totalSegundos % 60;

    return t; // Retorna a struct inteira preenchida
}

int main() {
    struct Tempo resultado;
    int total;

    // Entrada direta do total de segundos
    scanf("%d", &total);

    // Chamada da função de conversão
    resultado = converterSegundos(total);

    // Saída formatada conforme o exemplo
    printf("%dh %dmin %ds\n", resultado.horas, resultado.minutos, resultado.segundos);

    return 0;
}