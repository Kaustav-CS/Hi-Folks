
# Python program to find H.C.F of two numbers

print("Enter two Integers to find Highest Common Factor (lengthy process)\n")

# define a function
def c_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input('Enter your 1st number:  '))
num2 = int(input('Enter your 2nd number:  '))

print("The H.C.F. is", c_hcf(num1, num2))

exit()
