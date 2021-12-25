/* -O3 -march=core2 -msse2 */
#include <eigen3/Eigen/Dense>
#include <iostream>
#include <complex>
#include <ctime>
using namespace Eigen;
using namespace std;

typedef std::complex<double> dcp;
int main(){
  const int N = 200;
  ArrayXXd mat, mat2;
  ArrayXd v;
  clock_t t;
  size_t M = 10000;

  mat = ArrayXXd::Random(N, N);
  v = ArrayXd::Random(N);
  
  /* case 1 : broadcasting method */
  t = clock();
  for(size_t i = 0; i < M; i++){
    mat2 = mat.colwise() * v;
  }
  t = clock()-t;
  cout << " Broadcasting: " << (double)t / CLOCKS_PER_SEC  << endl;
  
  /* case 2 : Loop */
  t = clock();
  for(size_t i = 0; i < M; i++){
    for(size_t j = 0; j < N; j++)
      mat2.col(j) = mat.col(j)*v;
  }
  t = clock()-t;
  cout << " Loop: " << (double)t / CLOCKS_PER_SEC  << endl;

  /* case 3 :  optimized diagonal multiplication */
  t = clock();
  for(size_t i = 0; i < M; i++){
    mat2 = v.matrix().asDiagonal() * mat.matrix();
  }
  t = clock()-t;
  cout << " optimized diagonal: " << (double)t / CLOCKS_PER_SEC  << endl;

  /* case 4 : repmat */
  t = clock();
  for(size_t i = 0; i < M; i++){
    ArrayXXd vt = v.replicate(1, N);
    mat2 = vt*mat;
  }
  t = clock()-t;
  cout << " repmat: " << (double)t / CLOCKS_PER_SEC  << endl;

 /* case 5 :  repmat++ */
  t = clock();
  ArrayXXd vt = v.replicate(1, N);
  for(size_t i = 0; i < M; i++){
    mat2 = vt*mat;
  }
  t = clock()-t;
  cout << " repmat++: " << (double)t / CLOCKS_PER_SEC  << endl;
  
  return 0;
}
