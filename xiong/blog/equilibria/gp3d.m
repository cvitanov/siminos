function y=gp3d(a, x, dt, fn, step, ntot)
%
% function y=gp3d(a, x, dt, fn, step, ntot)
% rearrange date for gnuplot to draw 3d color map.
% input:
%				a: real and imaginary part of Fourier modes.
%				x: x coordiate.
%				dt: time step h
%				fn: file name
%				step: jump step for storing data.
%				ntot: larges index.

if ntot< size(a,2), a=a(:,1:step:ntot);
else a=a(:,1:step:end);
end

a=[zeros(1,size(a,2)); a(1:2:end-1, :)+1i*a(2:2:end, :);  ...
zeros(1,size(a,2)); a(end-1:-2:1, :)-1i*a(end:-2:2, :)];
a=real(ifft(a));
s=size(a);
t=0:dt*step:dt*step*(s(2)-1);
tt=repmat(t,s(1),1); xx=repmat(x,1,s(2));

fid=fopen(fn,'w');

for ii=1:s(2)
	%dlmwrite(fn, [xx(:,ii), tt(:,ii), a(:,ii)], '-append');
	fprintf(fid,'%f\t%f\t%f\n', [xx(:,ii), tt(:,ii), a(:,ii)]');
	fprintf(fid, '\n');
end

fclose(fid);
