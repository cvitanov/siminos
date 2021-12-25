function [nor, largerr]=xdtest(N,M,mode)

if mode==1,
% test of xdper_eig() function
%Don't use large dimension, otherwise eig() will give out wrong answer.
%N=5; M=20;
x=rand(N,N*M); [G,Q]=hess_trian(x); [tM,tQ]=xdper_schur(G,Q,200,10^-20);
[pereig,ev]=xdper_eig(tM,tQ);
MM=eye(N); 
for i=1:M, MM=x(:,N*(i-1)+1:N*i)*MM; end
[v,d]=eig(MM); d=diag(d); d=[log(abs(d)), sign(d)]; % for complex vector, sign give the normalized value.
for i=1:N, v(:,i)=v(:,i)*v(1,i)'; v(:,i)=v(:,i)/norm(v(:,i)); end
A=[d,pereig]; B=[v,ev]; nor=A; largerr=B;

elseif mode==2,
%test of xdper_schur() and hess_trian() function
%N=30; M=3000;
x=rand(N,N*M); [g1,q1]=hess_trian(x); [g,q]=xdper_schur(g1,q1,200,10^-20);
err=zeros(N,N*M); nor=zeros(1,N*M);
for i=2:M
    err(:,(i-1)*N+1:i*N)=q(:,(i-1)*N+1:i*N)'*x(:,(i-1)*N+1:i*N)*q(:,(i-2)*N+1:(i-1)*N)-g(:,(i-1)*N+1:i*N);
end 
err(:,1:N)=q(:,1:N)'*x(:,1:N)*q(:,(M-1)*N+1:M*N)-g(:,1:N);
for i=1:M*N, nor(i)=norm(err(:,i)); end
largerr=max(nor);


elseif mode==3,
%test of xdper_schur() function
%N=30; M=3000;
x=zeros(N,N*M);Q=repmat(eye(N),1,M); 
for i=1:M-1, x(:,(i-1)*N+1:i*N)=triu(rand(N)); end, x(:,(M-1)*N+1:M*N)=triu(rand(N),-1);
[g,q]=xdper_schur(x,Q,100,10^-20);
err=zeros(N,N*M); nor=zeros(1,N*M);
for i=2:M
    err(:,(i-1)*N+1:i*N)=q(:,(i-1)*N+1:i*N)'*x(:,(i-1)*N+1:i*N)*q(:,(i-2)*N+1:(i-1)*N)-g(:,(i-1)*N+1:i*N);
end 
err(:,1:N)=q(:,1:N)'*x(:,1:N)*q(:,(M-1)*N+1:M*N)-g(:,1:N);
for i=1:M*N, nor(i)=norm(err(:,i)); end
largerr=max(nor);

else
% test of hess_trian() functin
%N=30; M=3000;
x=rand(N,N*M); [g,q]=hess_trian(x); err=zeros(N,N*M); nor=zeros(1,N*M);
for i=2:M
    err(:,(i-1)*N+1:i*N)=q(:,(i-1)*N+1:i*N)'*x(:,(i-1)*N+1:i*N)*q(:,(i-2)*N+1:(i-1)*N)-g(:,(i-1)*N+1:i*N);
end 
err(:,1:N)=q(:,1:N)'*x(:,1:N)*q(:,(M-1)*N+1:M*N)-g(:,1:N);
for i=1:M*N, nor(i)=norm(err(:,i)); end
largerr=max(nor);

end

end