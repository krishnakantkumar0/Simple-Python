#fibonacci 
a=0
b=1
n=input('how many terms')
print(a)
print(b)
for i in range(3,n+1):
	c=a+b
	a=b
	b=c
	print (c)

