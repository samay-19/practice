# 2. Fibonacci Series of Length b
# Function Name: fibonacci_series(length)
# Print the first b numbers in the Fibonacci series.
# If b is negative or zero, raise an appropriate exception.

# from logging import raiseExceptions

n=int(input('enter the length:'))
a,b=0,1
try:
    if n==0:
        print("Not valid input")
    elif n<0:
        raise ValueError("Invalid input,Enter a positive integer")
    elif n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    elif n > 2:
        print('The length of fib is', n)
        print(a, b, end=' ')
        for i in range(n - 2):
            c = a + b
            print(c, end=' ')
            a, b = b, c

except ValueError as e:
    print("Not valid input")
    print(e)

