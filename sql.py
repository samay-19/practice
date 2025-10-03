# Write program to count the number of occurrences of chars in a string

name = 'samay'
n2=''
for i in range(len(name)):
    n2=n2+name[len(name)-i-1]
print(n2)

d = {}
for i in name:
    d[i] = d.get(i,0)+1
print(d)
#convert the lists into a dictinory while making key as l2 and values as l
l=[1,2,3]
l2=['a','b','c']
d={}
for i in range(len(l2)):
    d[l2[i]]=l[i]
print(d)