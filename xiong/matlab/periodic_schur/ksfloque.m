index=9; mult=2;
%load the initial condition, length and prime period.
load ks22f90h25t100; T=ppo(index).T*mult; a0=ppo(index).a; d=L;
%load ks22f90h25t100; T=ppo(1).T*2; a0=ppo(1).a1; d=L;
clearvars -except T a0 d;  nstp=8000;h=T/nstp; np=1; nqr=2;
%a0=ones(30,1)*0.1; d=22; h=0.25/2; nstp=10000; np=2; nqr=1;
[tt,aa,daa]=ksfjaco(a0, d, h, nstp, np,nqr);

s1=size(daa,1); s2=size(daa,2)/s1;
%[M,Q]=hess_trian(daa);
%[tM,tQ]=xdper_schur(M,Q,500,10^-14); 
%[pereig,ve]=xdper_eig(tM,tQ,2000,500,10^-14); x=pereig(:,1)/T; y=pereig(:,2);


%
load 9flo4000.mat; v=flove; mag=[]; nor=zeros(s1,1);
for i=1:s2
    v=daa(:,(i-1)*s1+1:i*s1)*v;
    for j=1:s1, nor(j)=norm(v(:,j)); v(:,j)=v(:,j)*v(1,j)'; v(:,j)=v(:,j)/norm(v(:,j)); end 
    mag=[mag,log(nor)];
end
i=10; x=1; y=2; z=3;
plot3(aa(x,:),aa(y,:),aa(z,:)); hold on, 
quiver3(aa(x,1),aa(y,1),aa(z,1),flove(x,i),flove(y,i),flove(z,i),0.3);
%}