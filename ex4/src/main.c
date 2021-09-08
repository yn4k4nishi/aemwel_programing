#include "stdio.h"
#include "math.h"
#include "dichotomy.h"

int main(){

    double tolerance = 1.0e-4;
    
    double x_min = -PI;
    double x_max = PI;

    double y_min = 0.001;
    double y_max = 20.0;

    double x_step = (x_max - x_min) / 2000.0; // 位相の刻み幅
    double y_step = (y_max - y_min) / 2000.0;

    // printf("tolerance : %lf\n",tolerance);
    // printf("x : %lf ~ %lf\n",x_min,x_max);
    // printf("y : %lf ~ %lf\n",y_min,y_max);
    // printf("\n");

    printf("x, y\n");

    for (double x = x_min; x < x_max; x += x_step){
        
        for (double y = y_min; y < y_max - y_step; y += y_step ){
            double ans, t;
            if (dichotomy(x, y, y + y_step, tolerance, &ans)){
                f(x, ans, &t);
                printf("%lf, %lf, %lf\n", x, ans, t);
            }
        }
        

    }
    
    return 0;
}