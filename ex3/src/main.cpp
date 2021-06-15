#include <cmath>
#include <ios>
#include <iostream>
#include <iomanip>
#include "dichotomy.h"

int main(){
    double dy_num = 1000.0;

    double dx = 15.0 / 1000.0;
    double dy = 15.0 / dy_num;

    double error = 1.0e-4;

    std::cout << "x, y, vacumm, dielectric" << std::endl;

    for (double x = 0.0; x < 15; x += dx) {
        std::cout << std::fixed << std::setprecision(15) << x << ",,";
        std::cout << std::fixed << std::setprecision(15) << x << ",";
        std::cout << std::fixed << std::setprecision(15) << x / std::sqrt(eps_r) << std::endl;

        double dy = x / dy_num;
        for (double y = 0.0; y < x; y += dy) {
            double e0, e1;
            if( (!f(x, y, &e0)) || (!f(x, y+dy, &e1)) ){
                continue;
            }

            if( e0 * e1 < 0 ){
                double ans;
                if( dichotomy(x, y, y+dy, error, &ans) ){
                    // std::cout << x << " , " << ans << std::endl;
                    std::cout << std::fixed << std::setprecision(15) << x << ",";
                    std::cout << std::fixed << std::setprecision(15) << ans << std::endl;
                }
            }
        }    
    }

    return 0;
}
