#!/usr/bin/env wolframscript
(* ::Package:: *)

B={{3,-1,0,-1},{-1,3,-1,0},{0,-1,3,-1},{-1,0,-1,3}};
B1=Inverse[B];
A={{0,1,0,0},{0,0,1,0},{0,0,0,1},{1,0,0,0}};
L={};
ML={};
For[m1=-2,m1<=2,m1++,
For[m2=-2,m2<=2,m2++,
For[m3=-2,m3<=2,m3++,
For[m4=-2,m4<=2,m4++,
M={m1,m2,m3,m4};
X=B1.M;
t=0;
For[i=1,i<=Length[L],i++,
If[X==L[[i]]||X==A.L[[i]]||X==A.A.L[[i]]||X==A.A.A.L[[i]],
t=1;]
];
If[
X[[1]]>=-1/2&&X[[1]]<=1/2&&
X[[2]]>=-1/2&&X[[2]]<=1/2&&
X[[3]]>=-1/2&&X[[3]]<=1/2&&
X[[4]]>=-1/2&&X[[4]]<=1/2&&
t==0
(*&&(X[[1]]\[NotEqual]X[[3]]||X[[2]]\[NotEqual]X[[4]])*),
AppendTo[L,X];
AppendTo[ML,M]
(*Print["M="];
Print[M];
Print["X="];
Print[X]*)
]
]
]
]
]


L1={};
For[i=1,i<=Length[L],i++,
AppendTo[L1,Point[{L[[i,1]],L[[i,3]]}]];
AppendTo[L1,Point[{L[[i,2]],L[[i,4]]}]];
AppendTo[L1,Point[{L[[i,3]],L[[i,1]]}]];
AppendTo[L1,Point[{L[[i,4]],L[[i,2]]}]];
]


L2={};
For[i=1,i<=Length[L],i++,
AppendTo[L2,Line[{{L[[i,1]],L[[i,3]]},{L[[i,2]],L[[i,4]]}}]];
AppendTo[L2,Line[{{L[[i,2]],L[[i,4]]},{L[[i,3]],L[[i,1]]}}]];
AppendTo[L2,Line[{{L[[i,3]],L[[i,1]]},{L[[i,4]],L[[i,2]]}}]];
AppendTo[L2,Line[{{L[[i,4]],L[[i,2]]},{L[[i,1]],L[[i,3]]}}]];
]


Graphics[
{
Line[{{1/2,1/2},{1/2,-1/2}}],
Line[{{-1/2,-1/2},{1/2,-1/2}}],
Line[{{-1/2,-1/2},{-1/2,1/2}}],
Line[{{1/2,1/2},{-1/2,1/2}}],L1
},
Frame->True,GridLines->{{-0.5,0,0.5}, {-0.5,0,0.5}}
]


P={};
For[i=1,i<=Length[L1]/4,i++,
Print[i," ",ML[[i]]];
(*Print[ML[[i]]];*)
AppendTo[P,Graphics[{{Red,L2[[(i-1)*4+1]],L2[[(i-1)*4+2]],L2[[(i-1)*4+3]],L2[[(i-1)*4+4]]},
{L1[[(i-1)*4+1]],L1[[(i-1)*4+2]],L1[[(i-1)*4+3]],L1[[(i-1)*4+4]]}},
Frame->True,GridLines->{{-1,-0.5,0,0.5,1}, {-1,-0.5,0,0.5,1}},
PlotRange->{{-0.55,0.55},{-0.55,0.55}}]
]
];
P



