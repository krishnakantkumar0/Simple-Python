#factorial using recurtion
n=int(input('enter a number'))
def fact(n):
	if n==1:
		return n
	else:
		return n*fact(n-1)
