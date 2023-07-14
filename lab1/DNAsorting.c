#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Estrutura que armazena o código e o seu número de ordenação
typedef struct {
    char* codigo;
    int num;
} tupla;

void insertionSort(tupla* lista, int tam) {
    for (int i = 1; i < tam; i++) {
        int auxNum = lista[i].num;
        tupla aux = lista[i];
        int j = i - 1;
        while (j >= 0 && lista[j].num > auxNum) {
            lista[j + 1] = lista[j];
            j -= 1;
        }
        lista[j + 1] = aux;
    }
}

int main() {
    int M, n, m, t;
    scanf("%d", &M);
    for (int d = 0; d < M; d++) {
        getchar(); //Pula linha
        scanf("%d %d", &n, &m);
        tupla* l = (tupla*)malloc(m * sizeof(tupla));
        for (int c = 0; c < m; c++) {
            char s[51];
            scanf("%s", s);
            t = 0;
            //Calcula o número de ordenação
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if ((int)s[i] > (int)s[j]) {
                        t += 1;
                    }
                }
            }
            //Armazena o par na estrutura
            l[c].codigo = strdup(s);
            l[c].num = t;
        }
        //Ordena e exibe os códigos
        insertionSort(l, m);
        for (int i = 0; i < m; i++) {
            printf("%s\n", l[i].codigo);
        }

        //Só printa uma linha em branco caso não seja a última
        if (d != M - 1) {
            printf("\n");
        }
        for (int cod = 0; cod < m; cod++) {
            free(l[cod].codigo);
        }
        free(l);
    }
    return 0;
}