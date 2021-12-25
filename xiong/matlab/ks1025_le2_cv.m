%load the initial condition, length and prime period.
load ks22f90h25t100; T=ppo(1).T*2; v0=ppo(1).a; len=L;
clearvars -except T v0 len;

%initial setup. time step=0.205.
N=32; Ncol=15; np=800; h=T/np; nqr=4; nperiod1=1000; nperiod2=1000;
x=len*(1:N)'/N;
v0=v0(1:2:N-3)+1i*v0(2:2:N-2); v=[0;v0;0;conj(v0(end:-1:1))];
tt=0; vv=v;
%for even oder derivative, the wave number k(N/2) should not be
%zero, but in KS system, N/2 mode has very small amplitude, so
%we set v(N/2)=0 all the time, and set k(N/2)=0 for even oder derivative.
k=[0:N/2-1 0 -N/2+1:-1]'*2*pi/len; L=k.^2-k.^4;
g=0.5i*k*N; 

E=exp(h*L);E2=exp(h*L/2);
M=16; r=exp(1i*pi*((1:M)-0.5)/M);
LR=h*L(:,ones(M,1))+r(ones(N,1),:);
%Q,f1,f2 and f3 still have symmetry.
Q=h*real( mean((exp(LR/2)-1)./LR,  2)  );
f1=h*real( mean(  (-4-LR+exp(LR).*(4-3*LR+LR.^2))./LR.^3,  2));
f2=h*real( mean( (2+LR+exp(LR).*(-2+LR))./LR.^3 , 2 ) );
f3=h*real( mean( (-4-3*LR-LR.^2+exp(LR).*(4-LR))./LR.^3, 2) );

% calculate the orbit .
for n=1:np-1
    t=n*h;        
    Nv=g.*fft(real(ifft(v)).^2);        a=E2.*v+Q.*Nv;
    % a still has symmetry, thus its ifft() must be real
    Na=g.*fft(real(ifft(a)).^2);        b=E2.*v+Q.*Na;
    Nb=g.*fft(real(ifft(b)).^2);        c=E2.*a+Q.*(2*Nb-Nv);
    Nc=g.*fft(real(ifft(c)).^2);
    v=E.*v+Nv.*f1+2*(Na+Nb).*f2+Nc.*f3;
    vv=[vv,v];tt=[tt,t];
end
vv=[vv,vv(:,1)];


np=np/2; h=T/np; DQ=eye(N,Ncol);
g2=repmat(2*g,1,N); ts=fft(eye(N)); rr=[]; fe=[]; avfe=[]; 
E=exp(h*L);E2=exp(h*L/2);
M=16; r=exp(1i*pi*((1:M)-0.5)/M);
LR=h*L(:,ones(M,1))+r(ones(N,1),:);
Q=h*real( mean((exp(LR/2)-1)./LR,  2)  ); 
f1=h*real( mean(  (-4-LR+exp(LR).*(4-3*LR+LR.^2))./LR.^3,  2));
f2=h*real( mean( (2+LR+exp(LR).*(-2+LR))./LR.^3 , 2 ) );
f3=h*real( mean( (-4-3*LR-LR.^2+exp(LR).*(4-LR))./LR.^3, 2) );
E=repmat(E,1,N); E2=repmat(E2,1,N); Q=repmat(Q,1,N);
f1=repmat(f1,1,N); f2=repmat(f2,1,N); f3=repmat(f3,1,N);

FGS=[]; R=[];
for nn=1:nperiod1
    for n=1:np
        tmpv1=repmat(vv(:,2*n-1),1,N);
        tmpv2=repmat(vv(:,2*n),1,N);
        tmpv3=repmat(vv(:,2*n+1),1,N);  
        
        Nts=g2.*fft(real(ifft(tmpv1)).*real(ifft(ts)));
        a2=E2.*ts+Q.*Nts;            
        Na2=g2.*fft(real(ifft(tmpv2)).*real(ifft(a2)));
        b2=E2.*ts+Q.*Na2;
        Nb2=g2.*fft(real(ifft(tmpv2)).*real(ifft(b2)));
        c2=E2.*a2+Q.*(2*Nb2-Nts);
        Nc2=g2.*fft(real(ifft(tmpv3)).*real(ifft(c2)));
        ts=E.*ts+Nts.*f1+2*(Na2+Nb2).*f2+Nc2.*f3;
       
    
        if  mod(n,nqr)==0 
            ts=real(ifft(ts)); 
            [q,r]=qr(ts*DQ,0); DQ=q;          
            ts=fft(eye(N)); 
            fe=[fe,log(abs(diag(r)))/(h*nqr)];
            
            if nn==nperiod1
                FGS=[FGS,DQ];R=[R,r];
            end
        end
    
    end
    
    if mod(nn,5)==0  avfe=[avfe mean(fe,2)]; fe=[]; end 
end

Ct=eye(Ncol); sz=size(R); sz=sz(2)/Ncol; C=[]; C2=[];
for nn=1:nperiod2
    for n=0:sz-1
        Ct=R(:,(sz-n-1)*Ncol+1:(sz-n)*Ncol)\Ct; 
        for i=1:Ncol nor=norm(Ct(:,i)); Ct(:,i)=Ct(:,i)/nor; end
        if nn==nperiod2-1 C2=[Ct,C2]; end
        if nn==nperiod2 C=[Ct,C]; end
    end
    
end

CV=[];
for nn=1:sz
   tmpcv=FGS(:,(nn-1)*Ncol+1:nn*Ncol)*C(:,(nn-1)*Ncol+1:nn*Ncol);
   CV=[tmpcv,CV];
end

