clear all
clc

tw0 = [4.35443487e-01,   2.55718139e-16,   3.55754017e-01, 3.69921902e-02, ...
2.65780484e-01,   1.23087691e-01, 8.96316601e-02, 1.99746439e-01, ...
-5.05277891e-02, 9.44414104e-02, -3.97381177e-02, 1.50718227e-02, ...
-1.69870437e-02, -4.78697400e-03, -4.29874538e-03, -6.15070596e-03, ...
3.91009306e-04, -3.00081892e-03, 8.69737447e-04,  -7.44165447e-04, ...
4.23685427e-04, 1.94447859e-07, 1.19333832e-04, 1.01415612e-04, ... 
8.76041620e-06,   5.66807136e-05,  -1.10380807e-05, 1.74490878e-05,  ...
-7.02070045e-06,   2.11126404e-06]';

ftw = @(tw) [vksred(tw); SliceCond(tw)];

%[tw, fval, info] = fsolve(@vksred, tw0);%Get it precise
[tw, fval, info] = fsolve(ftw, tw0);%Get it precise

%fphi = @(phi) SliceCond(LieEl(phi)*tw);

%[phi,fval,info] = fsolve(fphi, 0); %Get it back onto slice if it moved out

%tw = LieEl(phi)*tw;

%Compute velocity gradients
n=length(tw);
fx=vksred(tw);
eps=1.e-8; % could be made better
twperturbp=tw;
twperturbm=tw;
Anum = zeros(n);
for i=1:n
twperturbp(i)=twperturbp(i)+eps;
twperturbm(i)=twperturbm(i)-eps;
Anum(:,i)=(vksred(twperturbp) - vksred(twperturbm))/(2*eps);
twperturbp(i)=tw(i);
twperturbm(i)=tw(i);
end;

AAnum = zeros(n);
for i=1:n
twperturbp(i)=twperturbp(i)+eps;
twperturbm(i)=twperturbm(i)-eps;
AAnum(:,i)=(vel(twperturbp) - vel(twperturbm))/(2*eps);
twperturbp(i)=tw(i);
twperturbm(i)=tw(i);
end;

AAanalytic = gradV(tw);
Aanalytic = gradVred(tw);
%A = Aanalytic;
A = Aanalytic;

[V, lambda] = eig(A);
lambda=eig(A);
lambdarealsorted = sort(real(lambda), 'descend');
i1 = find(lambdarealsorted(1)==real(lambda))(1);
#i2 = find(lambdarealsorted(3)==real(lambda))(1);
i2 = find(lambdarealsorted(6)==real(lambda))(1);
i3 = find(lambdarealsorted(5)==real(lambda))(1);
v1 = real(V(:, i1));

v2 = imag(V(:, i1));
%v2 = real(V(:, i2));

v3 = real(V(:, i2));
%v3 = real(V(:, i3));

%%Gram-Schmidt orthogonalization:
%v1o = v1/norm(v1);

%v2o = v2 - dot(v2,v1o)*v1o;
%v2o = v2o/norm(v2o);

%v3o = v3 - dot(v3,v1o)*v1o - dot(v3,v2o)*v2o;
%v3o = v3o/norm(v3o);

%Gram-Schmidt orthogonalization:
v2o = v2/norm(v2);

v1o = v1 - dot(v1,v2o)*v2o;
v1o = v1o/norm(v1o);

v3o = v3 - dot(v3,v1o)*v1o - dot(v3,v2o)*v2o;
v3o = v3o/norm(v3o);

%Statespace eigenbasis:
e1 = v1o; e2 = v2o; e3 = v3o; ee = [e1, e2, e3];
%e1 = v1; e2 = v2; e3 = v3; ee = [e1, e2, e3];

n = 5;
tf = 115;
i = 1;
xsol=0; uu=0;
%hold on
N = 20;

mu = real(lambda(i1));
nu = imag(lambda(i1));

%for phi = 0:2*pi/N:2*pi-2*pi/N
for phi = 0:2*(mu/nu)*pi/N:2*(mu/nu)*pi-2*(mu/nu)*pi/N
    %x0 = tw + 1e-6*(cos(phi)*e1 + sin(phi)*e2);
    x0 = tw + 1e-6*exp(phi)*e1;
    
    [xsol, uu, tt, taut] = ksETDRK4red(x0, tf);
    
    fname = ['data/xsol', num2str(i), '.dat'];
    save(fname,'xsol');
    delcomm = ["sed -i.bak -e '1,5d' ", fname]; %Delete first 5 lines of the text file
    system(delcomm);
    
    xsolrel = xsol - tw';
    xsolssp = ee'*xsolrel';
    xsolssp = xsolssp';
    
    fname = ['data/xsolssp', num2str(i), '.dat'];
    save(fname,'xsolssp');
    delcomm = ["sed -i.bak -e '1,5d' ", fname]; %Delete first 5 lines of the text file
    system(delcomm); %So that we can easily read it from python
    %plot3(xsolssp(:,1),xsolssp(:,2),xsolssp(:,3));
    i = i+1;
end
system('rm data/xsol*dat.bak')
%Save the other relative equilibrium in this projection:

tw1= [2.32900179177042e-17, 0.419185107640453, 0.177530724935696, ...
0.146282501219190, -0.421516319672415, 0.287443694911592, ...
0.0933649938222870, -0.320489299533689, -0.00580747467566936, ...
0.0162361128812925, 0.0493485521038562, 0.0269378819483284, ...
-0.0298815966184568, 0.00764867193425785, 0.00381954953196330, ...
-0.00509574672330880, -0.000346492806473284, -0.00191533222584679, ...
0.00126630256353163, 0.00123563778819157, -0.000513489812992672, ...
-4.76928288759806e-05, 2.22135119056738e-07, 9.94332807607478e-06, ...
1.31720259229251e-05, -6.81917084273278e-05, 1.31699038813821e-05, ...
2.57228901352395e-05, -3.27286075134879e-06, -1.76547598708647e-06]';
tw1 = LieEl(-pi/2)*tw1;

[tw1, fval, info] = fsolve(ftw, tw1);
%fphi = @(phi) SliceCond(LieEl(phi)*tw1);
%[phi,fval,info] = fsolve(fphi, 0); %Get it back onto slice if it moved out
%tw1 = LieEl(phi)*tw1;
tw1rel = tw1 - tw;

%Project this reqv onto the ssp basis:
tw1ssp = ee'*tw1rel;
fname = 'data/tw1ssp.dat';
save(fname, 'tw1ssp')
delcomm = ["sed -i.bak -e '1,5d' ", fname]; %Delete first 5 lines of the text file
system(delcomm);

load ../../../matlab/ruslan/ks22f90h25t100.mat; % Load Ruslan's solution database

nrpo = 3; %Which rpo? 3 in arxiv ver. 

rpo0 = rpo(nrpo).a; %Read the rpo data from the db 
Trpo = rpo(nrpo).T; %Read the period

rpo0 = LieEl(-pi/2)*rpo0; %Bring the solution onto the slice

[xsolred, uured, ttred, tautred] = ksETDRK4red(rpo0, 3*Trpo);
    
xsolrel = xsolred - tw';
xsolssp = ee'*xsolrel';
xsolssp = xsolssp';
    
fname = 'data/rposolsspred.dat';
save(fname,'xsolssp');
delcomm = ["sed -i.bak -e '1,5d' ", fname]; %Delete first 5 lines of the text file
system(delcomm); %So that we can easily read it from python
