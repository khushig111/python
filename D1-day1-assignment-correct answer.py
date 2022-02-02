# KHUSHI GUPTA
# Assignment Ques: Take multiple numbers through input and print the sum of the numbers.

a = [int (i) for i in input("Enter multiple values to get sum:- ").split()]
# YOU MAY ENTER -VE VALUES AS WELL
sum=0
for j in a:
    sum +=j #sum = sum +j
#   print (sum)   # here it will print sum in loop.
print (sum)

"""

OTHER WAY
from functools import reduce
x = [int (i) for i in input("Enter multiple values to get sum:- ").split()]
res = reduce(lambda a,b: a + b ,x)
print (res)

"""