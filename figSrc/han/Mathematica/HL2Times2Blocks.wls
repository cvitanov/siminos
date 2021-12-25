#!/usr/bin/env wolframscript
(* ::Package:: *)

U=Table[1/2*Exp[2*Pi*I*((i-1)(i1-1)+(j-1)(j1-1))/2],{i,2},{j,2},{i1,2},{j1,2}];
U1=Conjugate[Transpose[U,{3,4,1,2}]];
(*The unitary matrices(tensors) U and the corresponding conjugate tranpose*)


B=Table[KroneckerDelta[i,i1]*KroneckerDelta[j,j1]*5+
If[i>1,-1*KroneckerDelta[i-1,i1]*KroneckerDelta[j,j1],-1*KroneckerDelta[i+1,i1]*KroneckerDelta[j,j1]]+
If[i<2,-1*KroneckerDelta[i+1,i1]*KroneckerDelta[j,j1],-1*KroneckerDelta[i-1,i1]*KroneckerDelta[j,j1]]+
If[j<2,-1*KroneckerDelta[i,i1]*KroneckerDelta[j+1,j1],-1*KroneckerDelta[i,i1]*KroneckerDelta[j-1,j1]]+
If[j>1,-1*KroneckerDelta[i,i1]*KroneckerDelta[j-1,j1],-1*KroneckerDelta[i,i1]*KroneckerDelta[j+1,j1]]
,{i,2},{j,2},{i1,2},{j1,2}];
(*B is the circulant matrix(tensor)*)


B1=Table[Sum[B[[i,j,i2,j2]]*U1[[i2,j2,i1,j1]],{i2,2},{j2,2}],{i,2},{j,2},{i1,2},{j1,2}];
B1=Table[Sum[U[[i,j,i2,j2]]*B1[[i2,j2,i1,j1]],{i2,2},{j2,2}],{i,2},{j,2},{i1,2},{j1,2}];
(*B1 is the diagonalized B*)


R1=Table[If[B1[[i,j,i1,j1]]==0,0,1/B1[[i,j,i1,j1]]],{i,2},{j,2},{i1,2},{j1,2}];
(*R1 is the inverse of B1*)


Simplify[Table[Sum[R1[[i,j,i2,j2]]*B1[[i2,j2,i1,j1]],{i2,2},{j2,2}],{i,2},{j,2},{i1,2},{j1,2}]]
(*Check R1.B1 is a unit tensor*)


Simplify[Table[Sum[U1[[i,j,i2,j2]]*U[[i2,j2,i1,j1]],{i2,2},{j2,2}],{i,2},{j,2},{i1,2},{j1,2}]]
(*Check U1.U is a unit tensor*)


G=Table[Sum[R1[[i,j,i2,j2]]*U[[i2,j2,i1,j1]],{i2,2},{j2,2}],{i,2},{j,2},{i1,2},{j1,2}];
G=Table[Sum[U1[[i,j,i2,j2]]*G[[i2,j2,i1,j1]],{i2,2},{j2,2}],{i,2},{j,2},{i1,2},{j1,2}];
(*G is the Green's function*)


(*M={{1,1},{1,1}};*)


(*X=Simplify[Table[Sum[G[[i,j,i2,j2]]*M[[i2,j2]],{i2,2},{j2,2}],{i,2},{j,2}]]*)


(*s=0;*)


L={};


For[k1=-4,k1<5,k1++,
For[k2=-4,k2<5,k2++,
For[k3=-4,k3<5,k3++,
For[k4=-4,k4<5,k4++,
M={{k1,k2},{k3,k4}};
X=Simplify[Table[Sum[G[[i,j,i2,j2]]*M[[i2,j2]],{i2,2},{j2,2}],{i,2},{j,2}]];
If[
	X[[1,1]]<1/2&&X[[1,1]]>=-1/2&&
	X[[2,1]]<1/2&&X[[2,1]]>=-1/2&&
	X[[1,2]]<1/2&&X[[1,2]]>=-1/2&&
	X[[2,2]]<1/2&&X[[2,2]]>=-1/2,
	(*Print["M="];
	Print[M];
	Print["X="];
	Print[X];
	s++;*)
	L=Append[L,X];
	]
]
]
]
]
(*Print["s="];
Print[s]*)
(*L is a list of all admissible periodic 2 times 2 blocks*)


L1={};
For[i=1,i<=Length[L],i++,
L1=Append[L1,Point[{L[[i,2,1]],L[[i,1,2]],L[[i,1,1]]}]];
L1=Append[L1,Point[{L[[i,2,2]],L[[i,1,1]],L[[i,1,2]]}]];
L1=Append[L1,Point[{L[[i,1,1]],L[[i,2,2]],L[[i,2,1]]}]];
L1=Append[L1,Point[{L[[i,1,2]],L[[i,2,1]],L[[i,2,2]]}]];
]
(*L1 is the list of all points in the admissible blocks*)


Graphics3D[L1,Axes->True,AxesLabel->{"\!\(\*SubscriptBox[\(X\), \(l - 1, t\)]\)","\!\(\*SubscriptBox[\(X\), \(l, t - 1\)]\)","\!\(\*SubscriptBox[\(X\), \(l, t\)]\)"}]


(*ListPointPlot3D*)
