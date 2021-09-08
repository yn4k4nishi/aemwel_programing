#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#define PI 3.14159265358979323846

// 対象の関数
// ゼロ除算などの計算できない場合はfalseを返す
bool f(double x, double y, double *error){    
    
    // パラメータ
    double L_R = 1.0;
    double C_R = 1.0;
    double L_L = 5.0;
    double C_L = 1.0;

    double w2_se = 1.0 / L_R / C_L;
    double w2_sh = 1.0 / L_L / C_R;

    *error = cos(x) - 1.0 + y*y * L_R *C_R / 2.0 * ( 1- w2_se /y /y ) * ( 1- w2_sh /y /y );
    return true;
}

// 2分法
// xは固定で、yに関して
bool dichotomy(double x, double min_y, double max_y, double tolerance, double *ans){
    const int max_trials = 1e4;
    
    double t0, t1;
    f(x, min_y, &t0);
    f(x, max_y, &t1);

    if( t0 * t1 > 0 ){
        return false;
    }

    int num = 0;
    double mid_y = (max_y + min_y) / 2.0;
    f(x, mid_y, &t1);
    while (abs(t1) > tolerance) {
        f(x, min_y, &t0);
        f(x, mid_y, &t1);

        if( t0 * t1 >= 0 ){
            min_y = mid_y;
        }else {
            max_y = mid_y;
        }

        mid_y = (max_y + min_y) / 2.0;

        if(num > max_trials){
            return false;
        }

        num ++;
    }

    *ans = mid_y;
    return true;
}