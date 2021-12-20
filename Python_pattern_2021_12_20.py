#  Pattern in trinagle shape
#  Date:  20 th December, 2021
#  ০১ পৌষ,১৪২৮
#  
#  


#s = 'Today is Monday'
s = input('Enter any string:\n')
P = [s[:i] for i in range(len(s)+1)]

print(*(P+P[::-1]), sep = '\n')
