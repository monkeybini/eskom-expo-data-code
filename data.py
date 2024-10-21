import math
import matplotlib.pyplot as plt

from functools import lru_cache


#Other functions to help analyse behaviour of a(n)
def is_prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True

#returns smallest prime divisor
def smallest_prime(k):
	if k==1:
		return 1
	for i in range(2,k+1):
		if k%i==0 and is_prime(i)==True:
			return i
	return k

#returns largest prime divisor
def largest_prime(k):
	prime=1
	for i in range(2,k+1):
		if k%i==0 and is_prime(i)==True:
			prime=i
	return prime

#returns sum of prime divisors
def sum_of_primes(k):
	sum=0
	for i in range(2,k+1):
		if k%i==0 and is_prime(i)==True:
			sum+=i
	return sum




@lru_cache(maxsize=None)
#a(n) value for initial conditions a(h)=k
def a(n,k,h):
	if n<h:
		return 0
	if n==h:
		return k
	else:
		return a(n-1,k,h)+math.gcd(a(n-1,k,h),n)

def b(n,k,h):
	if n<=h:
		return 0
	return math.gcd(a(n-1,k,h),n)

#count all 1s produced by b(n) in a range
def count1s(n,k,h):
	count=0
	for i in range(1,n+1):
		if b(i,k,h)==1:
			count+=1
	return count

#count primes produced by b(n) in a range
def countps(n,k,h):
	count=0
	for i in range(1,n+1):
		if b(i,k,h)>1:
			count+=1
	return count

#sum of primes produced by b(n) in a range
def sump(n,k,h):
	count=0
	for i in range(1,n+1):
		if b(i,k,h)>1:
			count+=b(i,k,h)
	return count

#return list of divisors of n
def divisors(n):
	divs=[]
	for i in range(1,n+1):
		if n%i==0:
			divs.append(i)
	return divs
	
#return list of prime divisors of n
def primedivs(n):
	divs=[]
	for i in range(1,n+1):
		if n%i==0 and is_prime(i)==True:
			divs.append(i)
	return divs
prev=0

listn=[]
listbn=[]
listan = []

#Prints all a(n) values for all h<n <1000, 1<h <1000 and h<a(h) <1000
for h in range (1,1000):
	for k in range(h+1,1000):
		for n in range(h,1000):
			if a(n,k,h)%n:
				print(a(n,k,h), k, h)


xlist = []
#output list of a(n)
ylist = []

#graphs y=3x, y=2x and y=1.5x
ylist_3x = []
ylist_2x = []
ylist_23x = []

for i in range(1,10000):
	xlist.append(i)

	#getting list of values of a(n) for a(2)=2
	ylist.append(a(i,2,2))

	ylist_23x.append(3/2*i)
	ylist_2x.append(2*i)
	ylist_3x.append(3*i)



plt.plot(xlist,ylist)

plt.plot(xlist,ylist_3x, linestyle="dashed")
plt.plot(xlist,ylist_2x, linestyle="dashed")
plt.plot(xlist,ylist_23x, linestyle="dashed")


plt.grid()
plt.show()

