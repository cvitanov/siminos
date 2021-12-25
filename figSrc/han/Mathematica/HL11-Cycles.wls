#!/usr/bin/env wolframscript
(* ::Package:: *)

F1=ImplicitRegion[y>1/2 (3-Sqrt[5])(x)&&y-1<1/2 (3-Sqrt[5])(x-1)&&y-1>1/2 (3+Sqrt[5])(x-1)&&
	y<1/2 (3+Sqrt[5])(x),{x,y}];
F2=ImplicitRegion[y>1/2 (3-Sqrt[5])(x)&&y-1<1/2 (3-Sqrt[5])(x-1)&&y-1<1/2 (3+Sqrt[5])(x)&&
	y>1/2 (3+Sqrt[5])(x),{x,y}];
F3=ImplicitRegion[y<1/2 (3-Sqrt[5])(x)&&y>1/2 (3-Sqrt[5])(x-1)&&y-1>1/2 (3+Sqrt[5])(x-1)&&
	y<1/2 (3+Sqrt[5])(x),{x,y}];


l=11;


U=Table[1/Sqrt[11]*Exp[I*2*Pi/11*(i-1)*(j-1)],{i,1,11},{j,1,11}];


A=Table[3*KroneckerDelta[i,j]-KroneckerDelta[i,j-1]-KroneckerDelta[i,j+1]-KroneckerDelta[i,j-l+1]-KroneckerDelta[i,j+l-1],{i,1,l},{j,1,l}];


Lx={};
Lm={};


Do[
M={i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11};
X=Inverse[A].M;
XL={};
XI=1;
Do[AppendTo[XL,{X[[i]],X[[i+1]]}],{i,1,l-1}];
AppendTo[XL,{X[[l]],X[[1]]}];
For[j=1,j<=l,j++,
If[XL[[j]]\[Element]F1||XL[[j]]\[Element]F2||XL[[j]]\[Element]F3,1,XI=XI*0]];
If[XI==1,AppendTo[Lx,X];AppendTo[Lm,M]]
,{i1,-1,1,1},{i2,-1,1,1},{i3,-1,1,1},{i4,-1,1,1},{i5,-1,1,1}
,{i6,-1,1,1},{i7,-1,1,1},{i8,-1,1,1},{i9,-1,1,1},{i10,-1,1,1}
,{i11,-1,1,1}]


Lm1={};
Do[AppendTo[Lm1,U.Lm[[i]]],{i,1,Length[Lm]}];


L3={};
For[i=1,i<=Length[Lm],i++,
T=Table[{1/l*{0,1,2,3,4,5,6,7,8,9,10,11}[[j]],Re[Lm1[[i,j]]],Im[Lm1[[i,j]]]},{j,1,l}];
AppendTo[L3,T]
]


L1={};
For[i=1,i<=Length[Lm],i++,
T=Table[{1/l*{0,1,2,3,4,5,6,7,8,9,10,11}[[j]],Re[Lm1[[i,j]]]},{j,1,l}];
AppendTo[L1,T]
]


L2={};
For[i=1,i<=Length[Lm],i++,
T=Table[{1/l*{0,1,2,3,4,5,6,7,8,9,10,11}[[j]],Im[Lm1[[i,j]]]},{j,1,l}];
AppendTo[L2,T]
]


(*ListPlot[L1,AxesLabel->{k,"|Mtilde|"}]*)


ListPlot3D[L3,AxesLabel->{"k/11","Re[Mtilde]","Im[Mtilde]"}]
