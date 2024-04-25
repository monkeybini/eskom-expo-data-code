import math



def calc(n,k):
	prev = k
	nxt = 0
	for i in range(2,n+1):
		diff = math.gcd(i,prev)
		nxt = prev + diff
		
		if nxt>3*k/2:
			print(i,nxt,3*k/2+1,k,k/2+1)
			break
	
		prev = nxt

for j in range(4,1000,2):
	calc(j,j)


