#print decimal to binary
num=input('enter a number')
binary = []
while num != 0:
    a = num % 2
    binary.append(a)
    num = num / 2
print (binary[::-1])