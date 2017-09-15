#find L.C.M using recursion
print ('hi krishnakant welcome in python')
def lcm(x, y):
   if x > y:
       grt = x
   else:
       grt = y
   while(True):
       if((grt % x == 0) and (grt % y == 0)):
           lcm = grt
           break
       grt += 1
   return lcm
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print('LCM of', num1,"and", num2,"is", lcm(num1, num2))

