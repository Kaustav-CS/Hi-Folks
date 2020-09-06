# Function to find HCF the Using Euclidian algorithm
print("Enter Teo Integers to find Highest Common Factor(quick proces) \n")

def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

a=int(input('Enter 1st Number: \t'))
b=int(input('Enter 2nd Number: \t'))
hcf = compute_hcf(a, b)
print("The HCF is", hcf)


exit()
