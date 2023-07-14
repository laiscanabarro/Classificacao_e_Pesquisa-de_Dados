#include <stdio.h>
#include <stdlib.h>

long int swaps, aux[500000];

void merge(long int lista[],long int inicio, long int meio, long int fim){

    long int i, j, k;
    i = inicio;
    j = meio;
    k = inicio;
    
    while(i <= meio - 1 && j <= fim){
        if (lista[i] <= lista[j]){
            aux[k] = lista[i];
            k ++;
            i ++;
        }
        else{
            aux[k] = lista[j];
            swaps += meio - i;
            k ++;
            j ++;
        }
    }
    
    while(i <= meio - 1){
        aux[k] = lista[i];
        k++;
        i++;
    }
    
    while(j <= fim){
        aux[k] = lista[j];
        k++;
        j++;
    }
    
    for(i = inicio; i <= fim; i++){
        lista[i] = aux[i];
    }
}

void mergeSort(long int lista[], long int inicio, long int fim){
    long int meio;
    if(inicio < fim){
        meio = (inicio + fim) / 2;
        mergeSort(lista,inicio, meio);
        mergeSort(lista,meio+1,fim);
        merge(lista,inicio,meio+1,fim);
    }
}

int main() {
    long int n, i,l[500000];
    while (1) {
        scanf("%ld", &n);
        if (n == 0) break;
        for (i = 0; i < n; i++) {
            scanf("%ld", &l[i]);
        }
        swaps = 0;
        mergeSort(l, 0, n-1);
        printf("%ld\n", swaps);
    }

    return 0;
}