from __future__ import division
from math import *
import numpy as np
from operator import getitem
from fractions import *
import random



total = 0	

def SYMBOL(n,t0_q, t1_q, t2_q):
	for i in range (n+1):
		num_m = numer(particle_q(n,t2_q)) * denom(particle_q(n,t0_q)) * denom(particle_q(n+1,t1_q)) *denom(particle_q(n-1,t1_q)) * denom(particle_q(n,t1_q)) + denom(particle_q(n,t2_q)) * numer(particle_q(n,t0_q)) * denom(particle_q(n+1,t1_q)) *denom(particle_q(n-1,t1_q)) * denom(particle_q(n,t1_q))+ denom(particle_q(n,t2_q)) * denom(particle_q(n,t0_q)) * numer(particle_q(n+1,t1_q)) *denom(particle_q(n-1,t1_q)) * denom(particle_q(n,t1_q))+ denom(particle_q(n,t2_q)) * denom(particle_q(n,t0_q)) * denom(particle_q(n+1,t1_q)) *numer(particle_q(n-1,t1_q)) * denom(particle_q(n,t1_q))- denom(particle_q(n,t2_q)) * denom(particle_q(n,t0_q)) * denom(particle_q(n+1,t1_q)) *denom(particle_q(n-1,t1_q)) * s*numer(particle_q(n,t1_q))
		denom_m = denom(particle_q(n,t2_q)) * denom(particle_q(n,t0_q)) * denom(particle_q(n+1,t1_q)) *denom(particle_q(n-1,t1_q)) * denom(particle_q(n,t1_q))
		

		return round(num_m/denom_m)
def symbol(m):
	for sym in range (-s+1 , 3+1 ):
		
		if m == sym:
			M[sym+s-1] = M[sym+s-1]+1
		if m > 3 or m < -s + 1:
			print m
	return M


def rational(x):
	
	m = numer(x) // denom(x)
	num = numer(x) - m * denom(x)
	g = gcd(num,denom(x))
	num = num//g
	den = denom(x)//g

	return([num,den])

def rational_i(x):
	
	m = numer(x) // denom(x)
	
	num = numer(x) - m * denom(x)

	g = gcd(num,denom(x))
	num = num//g
	den = denom(x)//g

	return([num,den])
def numer(cord):
	return(cord[0]) 

def denom(cord):
	return(cord[1]) 

def generator(n):
	q =  [rational_i([random.randint(0,denominator),random.randint(1,denominator)])]
	p =  [rational_i([random.randint(0,denominator),random.randint(1,denominator)])]
	for i in range (1,n):
		q = q + [rational_i([random.randint(0,denominator),random.randint(1,denominator)])]
		p = p + [rational_i([random.randint(0,denominator),random.randint(1,denominator)])]
	return([[numer(q[-1]),denom(q[-1])]]+q+[[numer(q[0]),denom(q[0])]],[[numer(p[-1]),denom(p[-1])]]+p+[[numer(p[0]),denom(p[0])]])


def multiply(n ,q , p):
	num_q = numer(particle_p(n,p)) *denom(particle_q(n,q)) * denom(particle_q(n+1,q)) * denom(particle_q(n-1,q)) + (s-1)* numer(particle_q(n,q)) * denom(particle_p(n,p)) * denom(particle_q(n+1,q)) * denom(particle_q(n-1,q))- numer(particle_q(n+1,q)) * denom(particle_p(n,p)) *denom(particle_q(n,q)) * denom(particle_q(n-1,q)) - numer(particle_q(n-1,q))*denom(particle_p(n,p)) *denom(particle_q(n,q)) * denom(particle_q(n+1,q)) 
	
	den_q = denom(particle_p(n,p)) *denom(particle_q(n,q)) * denom(particle_q(n+1,q)) * denom(particle_q(n-1,q))

	num_p = numer(particle_p(n,p)) *denom(particle_q(n,q)) * denom(particle_q(n+1,q)) * denom(particle_q(n-1,q))+(s-2)* numer(particle_q(n,q)) * denom(particle_p(n,p)) * denom(particle_q(n+1,q)) * denom(particle_q(n-1,q))- numer(particle_q(n+1,q)) * denom(particle_p(n,p)) *denom(particle_q(n,q)) * denom(particle_q(n-1,q))- numer(particle_q(n-1,q))*denom(particle_p(n,p)) *denom(particle_q(n,q)) * denom(particle_q(n+1,q)) 
	
	den_p = denom(particle_p(n,p)) *denom(particle_q(n,q)) * denom(particle_q(n+1,q)) * denom(particle_q(n-1,q))

	return rational([num_q,den_q]),rational([num_p,den_p])

def particle_q(n,q):
	return q[n]


def particle_p(n,p):
	return p[n]

def one_step(n,q,p):
	t1, t2 = [], []
	t_q, t_p = [], []
	
	for i in range (1,n+1):
		t1,t2 = multiply(i,q,p)
		t_q = t_q + [t1]
		t_p = t_p + [t2]
		
	return [t_q[-1]]+t_q+[t_q[0]], [t_p[-1]]+t_p+[t_p[0]]


def map(n,q,p):
	t0_q, t0_p = q, p 
	
	for iter in range (1,length+1):
		t1_q, t1_p = one_step(n,t0_q, t0_p)
		
		t2_q, t2_p = one_step(n,t1_q,t1_p)
		m=SYMBOL(n,t0_q, t1_q, t2_q)
		symbol(m)
		t0_q, t0_p = t1_q, t1_p
		# if t0_q==q and t0_p==p:

			# print iter
			# break


			# if (iter== 1260 or iter==630 or iter == 3150 or iter==6300 ):# or iter ==50 ):
				

			# 	break
			# else:
			# 	print(iter,q,p)	
			# 	break

		
	return t0_q, t0_p



total = 0
length = 100000
s = 7 #variable
n = 20 #variable
points = 10 #variable
M = np.zeros(3+s)

denominator = 10000

for j in range(0,points):
	q, p = generator(n)
	map(n,q,p)
	



t1_q ,t1_p = one_step(n,q,p)
t2_q, t2_p = one_step(n,t1_q,t1_p)


for i in range (s+3):
	total = total + M[i]
	
for i in range (s+3):
	 M[i]= M[i]/total

normal=max(M)	 

for i in range (s+3):
	M[i]=M[i]/normal

for i in range (s+3):
	print(1/M[i])	

print(total)
print(M)



