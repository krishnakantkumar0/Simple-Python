#print decimal to binary
num = int(input('enter a number'))
binary = []
while num != 0:
    a = num % 2
binary.insert(0, a)
num = num / 2
print binary