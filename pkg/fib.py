from functools import reduce
# def fibo(n):
#     if n < 0:
#         print('input is not correct')
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
    
fibo = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]
