# How do you count the occurrences of each element in a list using a dictionary?
# from py3 import values

k=['w','x','y','z']
v=['a','b','c','d']
d={}
i=0
while i<len(k):
    d[k[i]]=v[i]
    i+=1
print(d)

# for i in range(len(k)):
#     if i<=len(v)-1:
#         d[k[i]]=v[i]
#     elif i>len(v)-1:
#         d[k[i]]=0
# print(d)
def cnt(l):
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
n=list(map(int,input("enter the list:").strip().split()))
print(cnt(n))

# Define a function do_nothing that does nothing when called.
# This function should be syntactically correct.
def do_nothing():
    pass
do_nothing()
invert a dictionary
d={'a': 1, 'b': 2, 'c': 3}
d2={'d':2,'c': 3,'e':5}
print(d|d2)

d1={}
for i,j in d.items():
    d1[j]=i
print(d1)
print(dict(zip(d.values(),d.keys())))

# How do you create a dictionary using a dictionary comprehension
# that maps numbers to their squares for numbers 1 through 5?
d={x:x*x for x in range(1,6)}
print(d)
# Write a Python function that accepts an arbitrary number of integers as input and returns their sum.
# sum_all(1, 2, 3)       o/p: 6
# sum_all(5, 10, 15, 20) o/p: 50
# sum_all()              o/p: 0
def sum_all(*args):
    s=0
    for i in args:
        s+=i
    print(s)
sum_all(1,2,3)
# Write a function greet_user that takes
# one required argument name, and
# two optional keyword arguments greeting (default: "Hello") and punctuation (default: "!").
# greet_user("Alice")
# o/p: "Hello, Alice!"
# greet_user("Bob", greeting="Hi")
# o/p: "Hi, Bob!"
# greet_user("Eve", punctuation=".")
# o/p: "Hello, Eve."
# greet_user("Sam", greeting="Good morning", punctuation="!")
# o/p: "Good morning, Sam!"
def greet_user(greeting="hello",punctuation="!"):
    s=input("enter your name:")
    print(greeting,s,punctuation)
greet_user("Alice")
greet_user(greeting="Hi")
greet_user(punctuation='.')
greet_user(greeting="Good morning", punctuation="!")



