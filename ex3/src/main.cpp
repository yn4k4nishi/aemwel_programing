#include <iostream>
#include "dichotomy.h"

int main(){
    double dx = 15.0 / 500.0;
    double dy = 15.0 / 50.0;

    double error = 1.0e-2;

    std::cout << "x , y" << std::endl;

    for (double x = 0.0; x < 15; x += dx) {
        for (double y = 0.0; y < 15; y += dy) {
            double e0, e1;
            if( (!f(x, y, &e0)) || (!f(x, y+dy, &e1)) ){
                continue;
            }

            if( e0 * e1 < 0 ){
                double ans;
                if( dichotomy(x, y, y+dy, error, &ans) ){
                    std::cout << x << " , " << ans << std::endl;
                }
            }
        }    
    }

    return 0;
}
