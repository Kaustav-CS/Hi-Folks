# Python Program to find the L.C.M. of two input number

print("Enter Two Integers to find Lowest Common Multiplier \n")

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input('Enter Your 1st Integer to find LCM: \n\t'))
num2 = int(input('Enter Your 2nd Integer to find LCM: \n\t'))

print("The L.C.M. is", compute_lcm(num1, num2))

exit()
