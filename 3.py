# Python Program to find the area of triangle

a = input('enter the first side: ')
b = input('enter the second side: ')
c = input('enter the third side: ')


# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
