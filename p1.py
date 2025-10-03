# Write a Python program that accepts two integers as input:
# a and b. Implement the following five functions using proper exception handling and logging:
# 1. Prime Numbers Between a and b
# Function Name: find_primes(a, b)
# Find and return all prime numbers between a and b.
# Swap if a > b.
# from mysql.connector.constants import flag_is_set
def find_primes(a,b):
    if a>b:
        a,b=b,a
    l=[]
    for j in range(a,b+1):
        n=j
        f=0
        for i in range(2,n):
            if n % i == 0:
                f=1
        if f==0:
            l.append(n)
    return l
n1=int(input("enter a number: "))
n2=int(input("enter b number: "))

if n1<=1 or n2<=1:
    print("enter a number more than 1")
else:
    print(find_primes(n1,n2))

# 3. Sum of Digits of a and b
# Function Name: sum_of_digits(n)
# Return the sum of digits of both a and b.
def sum_of_digits(a,b):
    s=0
    for i in range(a,b+1):
        s+=i
    return s
a=int(input("enter a number: "))
b=int(input("enter b number: "))
print(sum_of_digits(a,b))
# 4. Factorial of a and b
# Function Name: calculate_factorial(n)
# Compute the factorial of a and b.
def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
a=int(input("enter a positive integer"))
b=int(input("enter a positive integer"))
print(factorial(a)*factorial(b))
# If either number is negative, raise an error.
# 5. Count Even and Odd Numbers Between a and b
# Function Name: count_even_odd(a, b)
# Return the count of even and odd numbers in the range from a to b.
def count_eo(a,b):
    ce=0
    co=0
    for i in range(a,b+1):
        if i%2==0:
            ce+=1
        else:
            co+=1
    return ce,co
a=int(input("enter no."))
b=int(input("enter no."))
c,d=count_eo(a,b)
print(f' even count is {c}, and odd count is {d}')
#
#
