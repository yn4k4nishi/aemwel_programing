#include "stdio.h"
#include "math.h"
#include "dichotomy.h"

int main(){

    double tolerance = 1.0e-4;
    
    double x_min = -PI;
    double x_max = PI;

    double y_min = 0.0;
    double y_max = 10.0;

    double x_step = (x_max - x_min) / 1000.0; // 位相の刻み幅
    double y_step = (y_max - y_min) / 1000.0;

    printf("tolerance : %lf\n",tolerance);
    printf("x : %lf ~ %lf\n",x_min,x_max);
    printf("y : %lf ~ %lf\n",y_min,y_max);
    printf("\n");

    printf("x, y, e\n");

    for (double x = x_min; x < x_max ; x += x_step){
        
        for (double y = y_min; y < y_max; y += y_step ){
            double error, ans;
            if (dichotomy(x, y, y + y_step, tolerance, &ans)){
                printf("%lf, %lf, %lf\n", x, ans, error);
            }
        }
        

    }
    
    return 0;
}