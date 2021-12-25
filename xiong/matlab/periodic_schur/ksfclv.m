%load the initial condition, length and prime period.
load ks22f90h25t100; T=ppo(1).T*2; a0=ppo(1).a; d=L;
%load ks22f90h25t100; T=ppo(1).T*2; a0=ppo(1).a1; d=L;
clearvars -except T a0 d;  nstp=100;h=T/nstp; np=2; nqr=1; ntf=1000; ntb=40;
%a0=ones(30,1)*0.1; d=22; h=0.25/2; nstp=10000; np=2; nqr=1;
[tt,~,daa]=ksfjaco(a0, d, h, nstp, np,nqr);
s1=size(daa,1); s2=size(daa,2)/s1;
DQ=eye(s1); fe=[]; afe=[]; t=[]; FGS=[];R=[]; Rt=[]; 
for i=1:(ntf+ntb)
    if mod(i,100)==0, disp(i); end
    for j=1:s2
        da=daa(:,(j-1)*s1+1:j*s1);
        [q,r]=qr(da*DQ); q=q*diag(sign(diag(r))); r=diag(sign(diag(r)))*r;
        DQ=q;
        % i==ntf, FGS=[FGS,DQ];R=[r,R]; end  % inverse order of R.
        %if i> ntf, Rt=[r,Rt]; end
        fe=[fe,log(abs(diag(r)))/(h*nqr)];        
        %t=[t,((i-1)*s2+j)*h*nqr];
    end     
    afe=[afe,mean(fe,2)];
    fe=[]; % in order to improve efficiency.
end

%{
Ct=eye(s1); C=[]; C2=[];
for nn=1:ntb
    if mod(nn,10)==0, disp(nn); end
    for n=1:s2
        %rt=R(:,((n-1)*s1+1):(n*s1)); 
        rt=Rt(:,((nn-1)*s1*s2+(n-1)*s1+1):((nn-1)*s1*s2+n*s1)); 
        for i=1:s1, Ct(1:i,i)=rt(1:i,1:i)\Ct(1:i,i); end
        %{
        for i=1:4, Ct(1:i,i)=rt(1:i,1:i)\Ct(1:i,i); end
        for i=5:s1           
            [ctt,flag]=gmres(rt(1:i,1:i),Ct(1:i,i),i-1,10^-10,30); 
            Ct(1:i,i)=ctt; 
            if flag==1, disp([flag,nn,n]); end
        end
        %}
        Ct=normc(Ct);      
        if nn==ntb, C=[Ct,C]; end
        if nn==ntb-10, C2=[Ct,C2]; end
    end
end

CV=[];
for nn=1:s2
   tmpcv=FGS(:,(nn-1)*s1+1:nn*s1)*C(:,(nn-1)*s1+1:nn*s1);
   CV=[CV,tmpcv];
end
%}
