void 
init(FILE *pp1, FILE *pp2, float* restrict p1, float* restrict p2);

float
ksSO2(float* restrict x0, float* restrict t, float* restrict x, float dth,int nn, float* restrict st, float* restrict ct, float *dis);

float 
dot(float *x, float *y);

float 
dis2(float* restrict x, float* restrict y);

void
tangt(float* restrict x0, float* restrict t);

void
sctable(float* restrict st, float* restrict ct, float dth, int nn);

float
root(float* restrict t, float* restrict x, float* restrict xx, float th0, float *pth, int maxit, float tol);

#define OPENMP
