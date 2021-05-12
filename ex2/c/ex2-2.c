#include "stdio.h"
#include "complex.h"
#include "utils.h"

static const int size = 4;
double complex M[4][4]={
    {  3+4j, -9j , 6-5j, 8+1j },
    { -4+5j,  7  , 2+3j, 4+1j },
    {  7-3j, 4-7j, -3j , 5-3j },
    {  1+8j, 9-6j, 1-1j,  -3  }
};

void inverse(const int size, 
             const double complex input[size][size],
             double complex output[size][size]){
    
    double complex expand[size][size*2];
    
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){ // inputをコピー
            expand[i][j] = input[i][j];
        }

        for (int j = 0; j < size; j++){ // 単位行列を追加
            if(i == j){
                expand[i][size+j] = 1;
            }else{
                expand[i][size+j] = 0;
            }
        }
    }

    // 左下の成分を0にする
    for (int i = 0; i < size; i++){ // 先頭の成分を1に
        double complex t = expand[i][0];
        for (int j = 0; j < size*2; j++){
            expand[i][j] /= t;         
        }
    }

    for (int k = 1; k < size; k++){ 
        for (int i = k; i < size; i++){ // 列同士で引き算
            for (int j = 0; j < size*2; j++){
                expand[i][j] -= expand[k-1][j];         
            }
        }

        for (int i = k; i < size; i++){
            double complex t = expand[i][k];
            for (int j = 0; j < size*2; j++){
                expand[i][j] /= t;         
            }
        }
    }

    // 右上の成分を0にする
    
    
    printMatrix(size, size*2, expand);    

}

int main(){

    printf("M = \n");
    printMatrix(size, size, M);
    printf("\n");

    double complex inv_M[size][size];
    inverse(size, M, inv_M);

    return 0;
}
