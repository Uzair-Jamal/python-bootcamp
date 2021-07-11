#Q1:
mul = lambda x,y : x * y
print(mul(12,5))

#Q2:
from functools import reduce
fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2),[0,1])
                     
print(fib(10))

#Q3:
n1 = [3,5,7,89,9]
n2 = 2
divisible=list(map(lambda num:num*n2,n1))
print(' '.join(map(str,divisible)))

#Q4:

l1=[9,80,27,45,34,22,110,81]
l2=list(map(lambda n:n%9==0,l1))
l2=list(filter(lambda n:n%9==0,l1))
print(' '.join(map(str,l2)))

#Q5:
lst1=[45,6,8,87,76,45,12,47,41]
lst2=list(filter(lambda m:m%2==0,lst1))
print(len(lst2))

