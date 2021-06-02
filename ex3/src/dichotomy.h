#ifdef __cplusplus
extern "C" {
#endif

const static double eps_r = 3.2;

bool f(double x, double y, double *error);

bool dichotomy(double x, double min_y, double max_y, double error, double *ans);

#ifdef __cplusplus
}
#endif