#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
#include "diffvec.h"

/* openmp for parallelizing the code*/
#ifdef OPENMP
#include <omp.h>
#endif

/* SIMD to parallelize some instructions.*/
#include <x86intrin.h>

#define PI 3.14159265358979323846

const int N=30;
const int M1=4000*2;
const int M2=3000;

const int Nroot=9;
const float dth=0.01;

const int maxit=5;
const float tol=1.0e-7;

int 
main(){
  FILE * pp1, * pp2, *pc, *angDis;
  float *p1, *p2, *poinc, *ang;
  float *st, *ct;
  const int nn=ceil((2*PI/dth));

  p1=(float*)malloc(sizeof(float)*M1*N);
  p2=(float*)malloc(sizeof(float)*M2*N);
  poinc=(float*)malloc(sizeof(float)*M2*M1);
  ang=(float*)malloc(sizeof(float)*M2*3);

  st=(float*)malloc(sizeof(float)*nn*N/2);
  ct=(float*)malloc(sizeof(float)*nn*N/2);
  sctable(st,ct,dth,nn);
  
  pp1=fopen("ppo191.txt","r"); 
  pp2=fopen("ppo34.txt","r");
  init(pp1,pp2,p1,p2);
  
  #ifdef OPENMP
#pragma omp parallel for default(none) shared(p1,p2,poinc,ang,st,ct)
  #endif
  for(int i=0; i<M2; i++){
    float t[N],dis,mindis=100,minang;
    float *x2=p2+i*N; 
    int index=0;
    float *d=&dis;

    printf("i=%d\n",i);
    tangt(x2,t);
    for(int j=0; j<M1; j++){	
      float *x1=p1+j*N;
      float th;
      th=ksSO2(x2,t,x1, dth,nn,st,ct,d);
      poinc[i*M1+j]=th;
      if(mindis>dis){
	index=j;
	mindis=dis;
	minang=th;
      }
    }
    ang[3*i]=index+1; /*make the starting index 1.*/
    ang[3*i+1]=minang;
    ang[3*i+2]=mindis;
  }
  
  pc=fopen("poinc.txt","w");
  for(int i=0; i<M2; i++){
    for(int j=0; j<M1-1; j++){
	fprintf(pc,"%f\t",poinc[M1*i+j]);
    }
    fprintf(pc,"%f\n",poinc[M1*i+M1-1]);
  }
  angDis=fopen("angDis.txt","w");
  for(int i=0; i<M2; i++){
    fprintf(angDis,"%f\t%f\t%f\n", ang[3*i],ang[3*i+1],sqrt(ang[3*i+2]));
  }
  
  fclose(pp1);
  fclose(pp2);
  fclose(pc);
  fclose(angDis);
    
  return 0;
}

void 
init(FILE *pp1, FILE *pp2, float* restrict p1, float* restrict p2){
  for(int i=0; i<M1; i++){
	  for(int j=0; j<N-1; j++) fscanf(pp1,"%f\t",&p1[i*N+j]);
	  fscanf(pp1,"%f\n",&p1[i*N+N-1]);
  }
 
  for(int i=0; i<M2; i++){
	  for(int j=0; j<N-1; j++) fscanf(pp2,"%f\t",&p2[i*N+j]);
	  fscanf(pp2,"%f\n",&p1[i*N+N-1]);
  }
}

/*ksSO2(): return the angle and the smallest distance square.*/
float
ksSO2(float* restrict x0, float* restrict t, float* restrict x, float dth,int nn, float* restrict st, float* restrict ct, float *dis){
  float xx[N],xf[N],s,c,theta,err,d[Nroot],poinc[Nroot];
  int index=0;
  float sg0=0;
  float sg1=0;
  float *pth=&theta;

  for(int i=0; i<nn; i++){
    for(int k=0; k<N/2; k++){
      c=ct[i*N/2+k];
      s=st[i*N/2+k];
      xx[2*k]=c*x[2*k]+s*x[2*k+1];
      xx[2*k+1]=-s*x[2*k]+c*x[2*k+1];
    }
    sg1=dot(t,xx);
    if( sg0*sg1<0){
      err=root(t,x,xf,dth*i,pth,maxit,tol);
      d[index]=dis2(x0,xf);
      poinc[index++]=*pth;
    }
    sg0=sg1;
  }
  float mind=d[0];
  int minindex=0;
  for(int i=1; i<index; i++){
    if(mind>d[i]){
      mind=d[i];
      minindex=i;
    }
  }
  
  *dis=mind;
  return poinc[minindex];
}

float 
dot(float *x, float *y){
  float sum;
  __m128 s=_mm_setzero_ps();
  __m128 a,b,lo;
  for(int i=0;i<N-3;i+=4){
    a=_mm_loadu_ps(&x[i]);
    b=_mm_loadu_ps(&y[i]);
    s=_mm_add_ps(s,_mm_mul_ps(a,b));
  }
  a=_mm_unpacklo_ps(s,s);
  b=_mm_unpackhi_ps(s,s);
  lo=_mm_add_ps(_mm_unpacklo_ps(a,a),_mm_unpackhi_ps(a,a));
  s=_mm_add_ps(_mm_unpacklo_ps(b,b),_mm_unpackhi_ps(b,b));
  s=_mm_add_ps(s,lo);
  
  sum=_mm_cvtss_f32(s);
  sum=sum+x[N-2]*y[N-2]+x[N-1]*y[N-1];
  
  return sum;
}

float 
dis2(float* restrict x, float* restrict y){
  float d=0,s;
  for(int i=0; i<N; i++){
    s=x[i]-y[i];
    d+=s*s;
  }
  return d;
}

void
tangt(float* restrict x0, float* restrict t){
  for(int i=0; i<N/2; i++){
    t[2*i]=(i+1)*x0[2*i+1];
    t[2*i+1]=-(i+1)*x0[2*i];
  }
  
}

void
sctable(float* restrict st, float* restrict ct, float dth, int nn){

  for(int i=0; i<nn; i++){
    float th=i*dth;    
    for(int j=0; j<N/2; j++){
      int index=i*N/2+j;
      float ang=(j+1)*th;
      st[index]=sin(ang);
      ct[index]=cos(ang);
    }
  }
}

/*Halley's algorithm for roots finding.*/
float
root(float* restrict t, float* restrict x, float* restrict xx, float th0, float *pth, int maxit, float tol){
  float tx[N],ttx[N];
  float s,c;
  float th=th0;
  float f,df,ddf,dth;
  int i;
  for(i=0; i<maxit; i++){
    for(int k=0; k<N/2; k++){
      c=cos(th*(k+1));
      s=sin(th*(k+1));
      xx[2*k]=c*x[2*k]+s*x[2*k+1];
      xx[2*k+1]=-s*x[2*k]+c*x[2*k+1];
      tx[2*k]=(k+1)*xx[2*k+1];
      tx[2*k+1]=-(k+1)*xx[2*k];
      ttx[2*k]=(k+1)*tx[2*k+1];
      ttx[2*k+1]=-(k+1)*tx[2*k];
    }
    f=dot(t,xx);
    df=dot(t,tx);
    ddf=dot(t,ttx);
    dth=-2*f*df/(2*df*df-f*ddf);
    th+=dth;
    //    printf("%d\t%e\t%.16e\n",i,fabs(f),dth);
    if(fabs(f)<tol) break;
  }
  *pth=th;

  return f;
}
