function [pereig,Ev]=xdper_eig(M,Q,np,nptr,eps)
%function [pereig,Ev]=xdper_eig(M,Q) calculates the eigenvalues and 
%eigenvectors of sequence of matrices M. 
%input:
%       M: periodic schur form of matrices. M1, M2,...Mm. the first m-1
%           matrices are upper-triangular. Mm is quasi-upper triangular with
%           a 1x1 block for each real eigenvalue and a 2x2 block for each pair
%           of conjugate eigenvalues.
%       Q: orthogonal matrices.
%       np: the maximal number of iteration
%       nptr: the number of iteration for transient stage when eigenvectors
%           are complex
%       eps: tolerance.
%output:
%       pereig: eigenvalues.
%               left column is the logrithm of magnitude.
%               right column is the sign of eigenvalue. For complex number,
%               it is normalized.
%       Ev: eigenvectors.
    n=size(M,1); m=size(M,2)/n;  pereig=[];  Ev=eye(n);   
    j=1;   
    while j<n        
        if M(j+1,(m-1)*n+j)==0, mhess=0; sig=1; % deal with real eigenvalue.
            for k=1:m,
                nor=abs(M(j,(k-1)*n+j)); sig=sig*sign(M(j,(k-1)*n+j)); mhess=log(nor)+mhess;  
            end 
            pereig=[pereig;[mhess,sig]]; j=j+1;
        else  % complex conjugate pair
             mhess=eye(2); mag=0;
             for k=1:m
                 mhess=M(j:j+1,(k-1)*n+j:(k-1)*n+j+1)*mhess;
                 nor=max(max(abs(mhess))); mag=mag+log(nor); 
                 mhess=mhess/nor;
             end
             cplx=eig(mhess); mag2=abs(cplx); cplx=cplx./mag2; mag=mag+log(mag2);
             pereig=[pereig; [mag,cplx]]; j=j+2;
        end
    end
    % deal with the last diagonal element of Mm.
    if M(n,(m-1)*n+n-1)==0,   mhess=0; sig=1;
         for k=1:m
             nor=abs(M(n,k*n)); sig=sig*sign(M(n,(k*n))); mhess=log(nor)+mhess;  
         end 
         pereig=[pereig;[mhess,sig]];
    end
%----------------------------------------------------------------------
    % calculate eigenvectors.    
    if nargin>=2,
        if nargin<5, eps=10^-15; end,
        if nargin<4, nptr=500; end, if nargin<3, np=2000; end
        j=1;
        while j<n            
            if M(j+1,(m-1)*n+j)==0 % deal with real eigenvector.
                conv=0;
                xj=zeros(n,1); xj(j)=1.0; xjt=xj;              
                for k=1:np,
                      for i=m:-1:1, xj=M(:,(i-1)*n+1:i*n)\xj; xj=xj/norm(xj); end,
                      if mod(k,50)==0, 
                        if norm(xj-xjt)<eps,conv=1; fprintf(1,'converge at power iteration k= %d\n', k); break,
                        else xjt=xj;
                        end    
                      end
                end 
                if conv==0,
                xjp=xj; xjt=xj;
                for k=1:np,
                    mag=0; 
                    for i=m:-1:1,
                        xj=M(:,(i-1)*n+1:i*n)\xj; nor=norm(xj); mag=mag+log(nor); xj=xj/nor;
                    end,                    
                    if mod(k,50)==0, 
                        if norm(xj-xjt)<eps,break,
                        else xjt=xj;
                        end    
                    end                    
                    del=-pereig(j-1,1)-mag;
                    if del <0 && del > log(eps), shift=-exp(del)/pereig(j-1,2);
                    else shift=0;
                    end
                    if mod(k,200)==0, disp(shift); end                   
                    xj=xj+shift*xjp; xj=xj/norm(xj); xjp=xj;                   
                    %xj=xj+xjp; xj=xj/norm(xj); xjp=xj;
                end
                end
                Ev(:,j)=xj; j=j+1; disp(k);
            else   % deal with complex eigenvector pairs.       
                %transient evolution  => converge to the n*2 subspace.
                xj=zeros(n,1); xj(j)=1.0; 
                for k=1:nptr, for i=m:-1:1, xj=M(:,(i-1)*n+1:i*n)\xj; xj=xj/norm(xj); end, end                
                xj1=xj; xj2=xj; xjp1=xj1; xjp2=xj2; xjt1=xj1; xjt2=xj2;
                for k=1:np                  
                    for i=m:-1:1
                        xj1=M(:,(i-1)*n+1:i*n)\xj1; xj1=xj1*xj1(1)'; xj1=xj1/norm(xj1);                        
                        xj2=M(:,(i-1)*n+1:i*n)\xj2; xj2=xj2*xj2(1)'; xj2=xj2/norm(xj2);                        
                    end
                    if mod(k,50)==0,
                        if norm(xj1-xjt1)<eps && norm(xj2-xjt2)<eps, break,
                        else xjt1=xj1; xjt2=xj2;
                        end
                    end 
                    %keep the first element to be real.
                    xj1=xj1+1i*xjp1; xj1=xj1*xj1(1)'; xj1=xj1/norm(xj1); xjp1=xj1; 
                    xj2=xj2-1i*xjp2; xj2=xj2*xj2(1)'; xj2=xj2/norm(xj2); xjp2=xj2; 
                end
                Ev(:,j)=xj1; Ev(:,j+1)=xj2; j=j+2; disp(k);              
            end
        end
        
       % deal with the last diagonal element of Mm.
        if M(n,(m-1)*n+n-1)==0
            xj=zeros(n,1); xj(n)=1.0; xjt=xj;
            for k=1:np,
                for i=m:-1:1, xj=M(:,(i-1)*n+1:i*n)\xj; xj=xj/norm(xj); end,
                if mod(k,50)==0, 
                        if norm(xj-xjt)<eps,break,
                        else xjt=xj;
                        end    
                end                    
            end
            Ev(:,n)=xj; disp(k);
        end        
    %calculate the eigenvectors.
    Ev=Q(:,(m-1)*n+1:m*n)*Ev;
    %transform the first element to be real.
    for i=1:n, Ev(:,i)=Ev(:,i)*Ev(1,i)'; Ev(:,i)=Ev(:,i)/norm(Ev(:,i)); end
    end
end