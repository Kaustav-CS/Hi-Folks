# Python program to find the L.C.M. of two input number

print('::Enter Two Numbers to find LCM::')
# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = float(input('Enter 1st Number to find LCM: \n\t'))
num2 = float(input('Enter 2nd Number to find LCM: \n\t')) 

print("The L.C.M. is", compute_lcm(num1, num2))

quit()
exit()
