# Number addition
print('Enter Two Numbers for addition')
try:
    n1=input('Enter 1st number: \t')
    n2=input('Enter 2nd number: \t')

    sum=float(n1)+float(n2)

    print('The sum of {0} and {1} is {2}'. format(n1,n2,sum))
except:
    print('Error, Invalid input')
exit()
