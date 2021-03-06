#ifndef KSSOLVER_H
#define KSSOLVER_H

const int N = 32; // truncation number.

#ifdef __cplusplus
extern "C"{
#endif

/********         function declaration               ***********/

/**
   @brief KS solver without calculating Jacobian matrix.
   
   @param[in] a0 initial condition, size N-2 array
   @param[in] d the lenth of the KS system
   @param[in] h time step
   @param[in] nstp number of steps to be integrated
   @param[in] np state saving spacing.
   @param[out] aa saved state vector size = (nstp/np)*(N-2)
*/
  void
  ksf(double *a0, double d, double h, int nstp, int np, double *aa);

/**
   @brief KS solver with calculating Jacobian (size (N-2)*(N-2)).

   @param[in] nqr Jacobian saving spacing spacing
   @param[out] daa saved Jacobian matrix. size = (nstp/nqr)*(N-2)*(N-2).
   Row-wise saved for each Jacobian.
*/
  void
  ksfj(double *a0, double d, double h, int nstp, int np, int nqr, double *aa, double *daa);

#ifdef __cplusplus
} // extern "C"
#endif

#endif /* KSSOLVER_H */
