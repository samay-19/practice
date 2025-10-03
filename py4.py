# print('hello')
# Accept user input through a loop and print the value.
# Break out of the loop when user enters a digit.
#
# WAFunction to find the sum of digits in the input string eg i/p:'H5rt586ibdi8'
def sod():
    n=input()
    s=0
    for i in n:
        if i.isdigit():
            s=s+int(i)
    print(s)
sod()

# Convert two lists into a dictionary
keys = ['one', 'Two', 'Three']
values = [1, 2, 3]
d=dict(zip(keys,values))
print(d)
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)
# # Write a function that accepts 2 i/p numbers and returns both sum and difference.
def sd():
    n1=int(input("enter first number"))
    n2=int(input("enter a number"))
    return f'sum is {n1+n2} and diff is {n1-n2}'
s=sd()
print(s)
# Iterate a given list and check if a given element
# exists as a key’s value in a dictionary. If not, delete it from the list
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
new=[]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
for i in roll_number:
    if i in sample_dict.values():
        new.append(i)
print(new)


#
# WAP to return - seperated output of the user input.
# i/p: Mike
#  o/p: M-i-k-e
n='mike'
l=[]
for i in n:
    l.append(i)
l='-'.join(l)
print(l)

# Turn every item of a list into its square
l=[ 5, 6, 7]
l2=[i*i for i in l]
print(l2)
l1=[ 5, 6, 7]
l3=[]
for i in l:
    i=i*i
    l3.append(i)
print(l3,end=' ')
# [25, 36, 49]

#
# WAP to insert the user input in the nth place in the list. Give an error message if not possible
li=[3,5,2,6,8,9,6,3,5]

li.insert(2,9)
#
