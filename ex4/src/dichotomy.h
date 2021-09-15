#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#define PI 3.14159265358979323846

// 対象の関数
// ゼロ除算などの計算できない場合はfalseを返す
bool f(double x, double y, double *error){    
    
    // パラメータ

    // double L_R = 1.0;
    // double C_R = 1.0;
    // double L_L = 5.0;
    // double C_L = 1.0;

    // double w2_se = 1.0 / L_R / C_L;
    // double w2_sh = 1.0 / L_L / C_R;

    // *error = cos(x) - 1.0 + y*y * L_R *C_R / 2.0 * ( 1- w2_se /y /y ) * ( 1- w2_sh /y /y );
    
    double Z_0 = 75.0;
    double Y_0 = 1.0 / Z_0;

    double w = 2.0 * PI * y;
    double L_0 = 13.2e-9;
    double C_0 = 0.5e-12;
    double v = w * sqrt(L_0 * C_0);
    double v_0 = 2.0 * PI * 1.5e9 * sqrt(L_0 * C_0);
    double d = 0.25 * v_0 / 2.0 / PI / 1.5e9;
    double theta = w * d / v; // @1.5GHz

    double Z = 1.0 / w / C_0;
    double Y = 1.0 / w / L_0;
    double ZY = -Z * Y;


    *error = cos(x) - cos(theta) - ZY / 2.0 * cos(theta/2.0) * cos(theta/2.0) - 1.0/2.0 * ( Z/Z_0 + Y/Y_0 ) * sin(theta) ;
    
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