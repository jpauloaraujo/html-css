#include <stdio.h>
#include <string.h>

typedef enum {
    DINHEIRO = 1,
    CARTAO,
    PIX
} TipoPagamento;

typedef union {

    struct {
        float valorRecebido;
        float valorCompra;
    } dinheiro;

    struct {
        float valorCompra;
        int parcelas;
    } cartao;

    struct {
        float valorCompra;
    } pix;

} DadosPagamento;

typedef struct {
    char nome[50];
    TipoPagamento tipo;
    DadosPagamento dados;
} Pagamento;

int main() {

    Pagamento p[3];

    float total = 0;
    int qtdDinheiro = 0;
    int qtdCartao = 0;
    int qtdPix = 0;

    for(int i = 0; i < 3; i++) {

        fgets(p[i].nome, 50, stdin);
        p[i].nome[strcspn(p[i].nome, "\n")] = '\0';

        scanf("%d", (int*)&p[i].tipo);

        float valorFinal = 0;
        int pagamentoValido = 1;

        if(p[i].tipo == DINHEIRO) {

            scanf("%f", &p[i].dados.dinheiro.valorRecebido);
            scanf("%f", &p[i].dados.dinheiro.valorCompra);

            if(p[i].dados.dinheiro.valorRecebido <
               p[i].dados.dinheiro.valorCompra) {

                printf("Pagamento insuficiente\n");
                pagamentoValido = 0;

            } else {

                valorFinal = p[i].dados.dinheiro.valorCompra;
                qtdDinheiro++;
            }

        } else if(p[i].tipo == CARTAO) {

            scanf("%f", &p[i].dados.cartao.valorCompra);
            scanf("%d", &p[i].dados.cartao.parcelas);

            valorFinal = p[i].dados.cartao.valorCompra;

            if(p[i].dados.cartao.parcelas > 3)
                valorFinal *= 1.05;

            qtdCartao++;

        } else if(p[i].tipo == PIX) {

            scanf("%f", &p[i].dados.pix.valorCompra);

            valorFinal = p[i].dados.pix.valorCompra;
            qtdPix++;
        }

        if(pagamentoValido) {

            printf("Cliente: %s\n", p[i].nome);
            printf("Valor final: R$ %.2f\n\n", valorFinal);

            total += valorFinal;
        }

        getchar(); // limpa buffer
    }

    printf("Total recebido: R$ %.2f\n", total);
    printf("Quantidade em dinheiro: %d\n", qtdDinheiro);
    printf("Quantidade no cartao: %d\n", qtdCartao);
    printf("Quantidade no pix: %d\n", qtdPix);

    return 0;
}