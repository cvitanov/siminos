from __future__ import division
from math import *
import numpy as np
from operator import getitem
from fractions import *
import random



total = 0	

def update_count(count,i,j,k,l,v,w):
	count[int(pow(s+3,a-1)*(i+s-1) + pow(s+3,a-2)*(j+s-1) + pow(s+3,a-3)*(k+s-1) +pow(s+3,a-4)*(l+s-1)) ] = count[int(pow(s+3,a-1)*(i+s-1) + pow(s+3,a-2)*(j+s-1) + pow(s+3,a-3)*(k+s-1) +pow(s+3,a-4)*(l+s-1) )] + 1
	return count

def two_SYMBOL(symbol_arr,count):
	
	for par in range (n-2):
		for r in range (0, length-4):
			i = int(symbol_arr[par][r])
			j = int(symbol_arr[par][r+1])
			k = int(symbol_arr[par+1][r])
			l = int(symbol_arr[par+1][r+1])
		
			count = update_count(count,i,j,k,l,v,w)
		
					

						
	
	return count
				



def SYMBOL(n,t0_q, t1_q, t2_q):
	for i in range (n+1):
		num_m = numer(particle_q(n,t2_q)) * denom(particle_q(n,t0_q)) * denom(particle_q(n+1,t1_q)) *denom(particle_q(n-1,t1_q)) * denom(particle_q(n,t1_q)) + denom(particle_q(n,t2_q)) * numer(particle_q(n,t0_q)) * denom(particle_q(n+1,t1_q)) *denom(particle_q(n-1,t1_q)) * denom(particle_q(n,t1_q))+ denom(particle_q(n,t2_q)) * denom(particle_q(n,t0_q)) * numer(particle_q(n+1,t1_q)) *denom(particle_q(n-1,t1_q)) * denom(particle_q(n,t1_q))+ denom(particle_q(n,t2_q)) * denom(particle_q(n,t0_q)) * denom(particle_q(n+1,t1_q)) *numer(particle_q(n-1,t1_q)) * denom(particle_q(n,t1_q))- denom(particle_q(n,t2_q)) * denom(particle_q(n,t0_q)) * denom(particle_q(n+1,t1_q)) *denom(particle_q(n-1,t1_q)) * s*numer(particle_q(n,t1_q))
		denom_m = denom(particle_q(n,t2_q)) * denom(particle_q(n,t0_q)) * denom(particle_q(n+1,t1_q)) *denom(particle_q(n-1,t1_q)) * denom(particle_q(n,t1_q))
		

		return [round(num_m/denom_m)]
def symbol(m,symbol_array):
	
	symbol_array = symbol_array + [m]
	

	for sym in range (-s+1 , 3+1 ):
		
		if m == sym:
			M[sym+s-1] = M[sym+s-1]+1
		if m > 3 or m < -s + 1:
			print m
		
	return M, symbol_array


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


def map(n,q,p,sym2):
	t0_q, t0_p = q, p 
	m =[[]]
	for i in range (1,n):
		m = m + [[]]

	
	for iter in range (1, length+1):
		t1_q, t1_p = one_step(n,t0_q, t0_p)
		
		t2_q, t2_p = one_step(n,t1_q,t1_p)
		
		for par in range (1, n+1):
			m[par-1] = SYMBOL(par, t0_q, t1_q, t2_q) + m[par-1]
			

		
		

		t0_q, t0_p = t1_q, t1_p

		
	return m
def organize(sym_list,m_particle):
	j = 0
	for i in range (1, n+1):
		while j < length:
			m_particle = m_particle + [sym_list[j]]
			j = j + n
	return m_particle



index = 0
total = 0
length = 10000
s = 7  #variable
n = 20 #variable
points = 10000
symbol_array = []
M = np.zeros(3+s)

denominator = 10000

m_particle = []
zero = []
count = []


a = 4 # constant

for i in range (0,int(pow(s+3,a))):	
	count = count + [0]
print count	


sym2 =[[]]
for i in range (1,n):
	sym2 = sym2 + [[]]


for j in range(0,points):
	q, p = generator(n)
	sym2 = map(n,q,p,sym2)
	
	count=two_SYMBOL(sym2,count)
	print(count)
	print(j) 
	print("***********")





TOTAL = sum(count)
for i in range (0,int(pow(s+3,a))):
	print(i, count[i]/TOTAL)



