import math



def is_prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True
def calc(n,k):
	prev = k
	nxt = 0
	for i in range(2,n+1):
		diff = math.gcd(i,prev)
		nxt = prev + diff
		
		if nxt>3*k/2 and nxt/i == 3 and diff>1:
			if is_prime(diff)==False:
				print("counter example found")
			print(i,nxt, diff,k)
			break
	
		prev = nxt

for j in range(4,10000,2):
	calc(2*j,j)


