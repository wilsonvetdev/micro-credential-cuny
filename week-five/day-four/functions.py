# s. trowbridge 2020
def square(n):
    return n*n

def cube(n):
    return n*n*n

def summation(n):
    sum=0
    for i in range(1, n+1):
        sum += i
    return sum

def factorial(n):
    product=1
    for i in range(1, n+1):
        product *= i
    return product
