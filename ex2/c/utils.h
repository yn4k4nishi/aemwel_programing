#include "stdio.h"
#include "complex.h"

// 虚数単位をjにする
#undef I
#define j _Imaginary_I

void printMatrix(int row, int col, double complex matrix[row][col]){
    for (int i = 0; i < row; i++){
        if( i == 0){
            printf("┏\t");
        }else if (i == row-1){
            printf("┗\t");
        }else{
            printf("┃\t");
        }

        for (int j = 0; j < col; j++){
            printf("%f%+fj\t", creal(matrix[i][j]), cimag(matrix[i][j]));
        }

        if( i == 0){
            printf("┓");
        }else if (i == row-1){
            printf("┛");
        }else{
            printf("┃ ");
        }
        printf("\n");
    }
}
