## Python program to display all the prime numbers within an interval

L =input('Enter Starting number of the nember set:\t')
lower=int(L)
#900
U =input('Enter Last number of the nember set:\t')
upper=int(U)
#1000

print("Prime numbers between", lower, "and", upper, "are:\t")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num )
quit()
