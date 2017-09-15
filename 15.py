binary = raw_input('enter 0s and 1: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print decimal
