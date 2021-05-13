#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "ctype.h"
#include "complex.h"
#include "stdbool.h"

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

// convert string to double complex 
double complex str2dc(const char* str){
    double real = 0.0;
    double imag = 0.0;

    // split real and imag
    char *e; // 変換不可の部分
    real = strtod(str, &e);
    
    char *p = strstr(e, "j");
    if(p != NULL){
        *p = ' ';
    }

    imag = strtod(e, NULL);
    
    double complex result = real + imag * 1j;
    return result;
}

static const int MAX_SIZE = 250;

void loadMatrix(char *file_path, int mat_size, double complex **mat){
    printf("load matrix : %s\n",file_path);
    
    FILE *fp;
    char buf[256];

    fp = fopen(file_path, "r");
    fgets(buf, MAX_SIZE, fp);

    // 行列のサイズを計算
    mat_size = 0;
    for (size_t i = 0; i < sizeof(buf); i++){
        if(buf[i] == ','){
            mat_size += 1;
        }else if(buf[i] == '\n'){
            mat_size += 1;
            break;
        }
    }

    double complex matrix[mat_size][mat_size]; 

    for (int i = 0; i < mat_size; i++){
        // str から double complex に変換
        char *t = strtok(buf, ",");
        printf("%s\n",t);
        matrix[i][0] = str2dc(t);
        int j = 1;
        while (true){
            t = strtok(NULL, ",\n");
            if(t == NULL){
                break;
            }
            printf("%s\n",t);
            matrix[i][j] = str2dc(t);
            j ++;
        }
    }

    fclose(fp);

    mat = matrix;
}
