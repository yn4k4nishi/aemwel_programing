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
    for (int k = 1; k < size; k++){
        for (int i = 0; i < k; i++){
            double complex t = expand[i][k];
            for (int j = 0; j < size*2; j++){
                expand[i][j] -= t * expand[k][j];
            }   
        }
    }
    
    // outputに結果をコピー
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            output[i][j] = expand[i][j+size];
        }
        
    }
}

/*
00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33
*/

void dot(const int size, 
         const double complex m1[size][size],
         const double complex m2[size][size],
         double complex result[size][size]){

    // r[0][0] = m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0] + m1[0][2]*m2[2][0] + m1[0][3]*m2[3][0];
    // r[0][1] = m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1] + m1[0][2]*m2[2][1] + m1[0][3]*m2[3][1];
    // r[1][0] = m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0] + m1[1][2]*m2[2][0] + m1[1][3]*m2[3][0];

    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            result[i][j] = 0.0;
            for (int k = 0; k < size; k++){
                result[i][j] += m1[i][k] * m2[k][j];
            }
            
        }
    }
}

int main(){

    printf("M = \n");
    printMatrix(size, size, M);
    printf("\n");

    double complex inv_M[size][size];
    inverse(size, M, inv_M);

    printf("inv M = \n");
    printMatrix(size, size, inv_M);
    printf("\n");

    double complex t[size][size];
    dot(size, M, inv_M, t);
    printf("M * inv M = \n");
    printMatrix(size, size, t);

    return 0;
}
