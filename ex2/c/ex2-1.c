#include "stdio.h"
#include "complex.h"

// 虚数単位をjにする
#undef I
#define j _Imaginary_I

double complex M[4][4]={
    {  3+4j, -9j , 6-5j, 8+1j },
    { -4+5j,  7  , 2+3j, 4+1j },
    {  7-3j, 4-7j, -3j , 5-3j },
    {  1+8j, 9-6j, 1-1j,  -3  }
};

void printMatrix(int size, double complex matrix[size][size]){
    for (int i = 0; i < size; i++){
        if( i == 0){
            printf("┏\t");
        }else if (i == size-1){
            printf("┗\t");
        }else{
            printf("┃\t");
        }

        for (int j = 0; j < size; j++){
            printf("%f%+fj\t", creal(matrix[i][j]), cimag(matrix[i][j]));
        }

        if( i == 0){
            printf("┓");
        }else if (i == size-1){
            printf("┛");
        }else{
            printf("┃ ");
        }
        printf("\n");
    }
    

}

double complex det2x2(double complex matrix[2][2]){
    return matrix[0][1] * matrix[1][0] - matrix[0][0] * matrix[1][1];
}

double complex det(int size, double complex matrix[size][size]){
    if(size == 2){
        return det2x2(matrix);
    }else{
        double complex ans = 0.0 + 0.0j; // 答え
        double complex a_mat[size-1][size-1]; //余因子行列
        
        for (int i = 0; i < size; i++){ // i列と0行を抜く
        
            // 余因子行列を作る
            for (int j = 0; j < size; j++){
                if(i > j){
                    for (int k = 0; k < size-1; k++){
                        a_mat[j][k] = matrix[j][k+1];
                    }
                }else if(i < j){
                    for (int k = 0; k < size-1; k++){
                        a_mat[j-1][k] = matrix[j][k+1];
                    }
                }
                
            }
            printf("\n");
            printMatrix(size-1, a_mat);
        }
        
    }
}

int main(int argc, char *argv[]){

    printf("M = \n");
    printMatrix(4, M);

    det(4, M);

    return 0;
}
