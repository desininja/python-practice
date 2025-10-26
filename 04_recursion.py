def fib(n):
    if n == 0:
        print(0)
        return
    if n == 1:
        print(0)
        print(1)
        return
    else:
        n1 = 0
        n2 = 1 
        print(n1)
        print(n2)
        for i in range(2,n):
            m = n2+n1
            print(m)
            n1 = n2
            n2=m
    return 

#fib(9)
        
"""
Fibonacci Series Revised
"""

def fib_revised(n):
    if n<=0:
        return
    n1,n2 = 0,1

    print(n1, end=" ")

    if n ==1:
        return
    print(n2, end= " ")

    for _ in range(2,n):
        next_fib = n1+n2 
        print(next_fib, end=" ")
        n1,n2 = n2, next_fib

#fib_revised(2)
        

def fib(n):
    #Base case of recursion
    if(n==0 or n==1):
        return n 
    
#     return fib(n-2) + fib(n-1)

# print(fib(6))



def fib(n):
    #Base case of recursion
    if(n==0 or n==1):
        return n 
    #print(fib(n-2)+fib(n-1))
    return fib(n-2) + fib(n-1)

#print(fib(6))




def recur_fib(n):

    if (n==0 or n==1):
        return n
    
    return recur_fib(n-1)+recur_fib(n-2)


#print(recur_fib(6))


def factorial(n):
    if n ==0:
        return 1
    if n >0:
        return n*factorial(n-1)
    
print(factorial(4))