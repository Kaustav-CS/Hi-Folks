# Python Program to find the factors of a number



# This function computes the factor of the argument passed
num = int(input("Enter Number to know the factors: \t"))
print('(you must have time)')
def print_factors(x):
      print("The factors of",x,"are:")
      for i in range(1, x + 1):
       if x % i == 0:
           print(i)



print_factors(num)

quit()


#time consuming process
