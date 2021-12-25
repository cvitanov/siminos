function [tt, aa, daa] = ksfjaco(a0, d, h, nstp, np,nqr)

%load the initial condition, length and prime period.
%load ks22f90h25t100; T=ppo(1).T*2; a0=ppo(1).a; d=L;
%clearvars -except T a0 d;  nstp=100;h=T/nstp; np=2; nqr=1;
%a0=ones(30,1)*0.1; d=22; h=0.25/2; nstp=10000; np=2; nqr=1;
 N = length(a0)+2;  Nh = N/2;  % N should be even (preferably power of 2)
 
 v = [zeros(1,N-1); [a0(1:2:end-1)+1i*a0(2:2:end) zeros(Nh-1,N-2)]; ...
         zeros(1,N-1); [a0(end-1:-2:1)-1i*a0(end:-2:2) zeros(Nh-1,N-2)]];
    v(N+2:2*N+1:end) = 1;  v(2*N+2:2*N+1:end) = 1i;
    v(2*N:2*N-1:end) = 1;  v(3*N:2*N-1:end) = -1i; 
  
  k = (2.*pi./d).*[0:Nh-1 0 -Nh+1:-1]';   % wave numbers
  L = k.^2 - k.^4;                        % Fourier multipliers
  E = exp(h*L);  E2 = exp(h*L/2);
  M = 16;                                 % no. of points for complex means
  r = exp(1i*pi*((1:M)-.5)/M);            % roots of unity
  LR = h*L(:,ones(M,1)) + r(ones(N,1),:); 
  Q = h*real(mean((exp(LR/2)-1)./LR ,2));
  f1 = h*real(mean((-4-LR+exp(LR).*(4-3*LR+LR.^2))./LR.^3 ,2));
  f2 = h*real(mean((2+LR+exp(LR).*(-2+LR))./LR.^3 ,2));
  f3 = h*real(mean((-4-3*LR-LR.^2+exp(LR).*(4-LR))./LR.^3 ,2));
  aa = a0;  tt = 0;  g = 0.5i*k*N;
  
    E =  repmat(E,1,N-1);   E2 = repmat(E2,1,N-1);  Q = repmat(Q,1,N-1);
    f1 = repmat(f1,1,N-1);  f2 = repmat(f2,1,N-1);  f3 = repmat(f3,1,N-1);
    g = [g repmat(2.*g,1,N-2)];
    
    %DQ=eye(N-2); fe=[];
    daa=[];
    for n = 1:nstp,
      t = n*h;                   rfv = real(ifft(v));   Nv = g.*fft(repmat(rfv(:,1),1,N-1).*rfv);
      a = E2.*v + Q.*Nv;         rfv = real(ifft(a));   Na = g.*fft(repmat(rfv(:,1),1,N-1).*rfv);
      b = E2.*v + Q.*Na;         rfv = real(ifft(b));   Nb = g.*fft(repmat(rfv(:,1),1,N-1).*rfv);
      c = E2.*a + Q.*(2*Nb-Nv);  rfv = real(ifft(c));   Nc = g.*fft(repmat(rfv(:,1),1,N-1).*rfv);
      v = E.*v + Nv.*f1 + 2*(Na+Nb).*f2 + Nc.*f3;
      
      if  mod(n,np)==0 && n < nstp, 
        y1 = [real(v(2:Nh,1)) imag(v(2:Nh,1))]';
        aa = [aa, y1(:)]; tt = [tt, t]; 
      end 
      
      if mod(n,nqr)==0 
        da = zeros(N-2,N-2);  da(1:2:end,:) = real(v(2:Nh,2:end));
        da(2:2:end,:) = imag(v(2:Nh,2:end)); daa=[daa,da];
        %[q,r]=qr(da*DQ); q=q*diag(sign(diag(r))); r=diag(sign(diag(r)))*r;
        %DQ=q;
        v(:,2:end)=0;
        v(N+2:2*N+1:end) = 1;  v(2*N+2:2*N+1:end) = 1i;
        v(2*N:2*N-1:end) = 1;  v(3*N:2*N-1:end) = -1i; 
       % fe=[fe,log(abs(diag(r)))/(h*nqr)];
      end
    end
  