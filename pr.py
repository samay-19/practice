# Write a Python program that accepts two integers as input:
# a and b. Implement the following five functions using proper exception
# handling and logging:
# 1. Prime Numbers Between a and b
# Function Name: find_primes(a, b)
# Find and return all prime numbers between a and b.
# Swap if a > b.
from pandas import concat


def is_prime(a,b):
    if a>b:
        a,b=b,a
    l=[]
    for i in range(a,b+1):
        n=i
        f=0
        for j in range(2,n):
            if n%j==0:
                f=1
                print(n,"is not a prime number",end="\n")
                break
        if f==0:
            print(n,"is a prime number",end="\n")
            l.append(n)
    return l

n1=int(input("enter a="))
n2=int(input("enter b="))
if n1<=1 or n2<=1:
    print("enter a valid number")
print(is_prime(n1,n2))



