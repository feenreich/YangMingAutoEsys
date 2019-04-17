#include<stdio.h>
#include<stdlib.h>

int main(){
    int T, N;
    char P[100010], A[100010];
    scanf("%d",&T);
    for(int i=0;i<T;i++){
        scanf("%d", &N);
        scanf("%s", P);
        for(int j=0;j<2*N-2;j++)
            A[j] = (P[j] == 'S')?'E':'S';
        A[2*N-2] = 0;
        printf("Case #%d: %s\n", i+1, A);
    }
}
