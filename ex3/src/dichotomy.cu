#include <stdio.h>
#include <math.h>
#include "dichotomy.h"

bool f(double x, double y, double *error){
    if( (-x*x + eps_r * y*y) < 0 ){
        return false;
    }

    if( (x*x - y*y) == 0 ){
        return false;
    }

    if( (-x*x + eps_r * y*y)/(x*x - y*y) < 0 ){
        return false;
    }

    *error = tan( sqrt( -x*x + eps_r * y*y ) ) - sqrt( ((-x*x + eps_r * y*y)/(x*x - y*y)) );
    return true;
}

bool dichotomy(double x, double min_y, double max_y, double error, double *ans){
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
    while (abs(t1) > error) {
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

    f(x, mid_y, ans);
    return true;
}