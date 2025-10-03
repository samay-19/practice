# 1.
# (a) How to find the maximum occurring character in given String.
name = 'samay'
d = {}
for i in name:
    d[i] = d.get(i,0)+1
m = d[name[0]]
ans = ''
for i in d:
    if d[i] >= m:
        ans = i
        m = d[i]
print(ans)
# (b) find non repeated char in a string.
for i in d:
    if d[i] == 1:
        print(i,end=' ')
print()
# (c) how to remove the duplicate character from String
s='samay'
s1=''
for i in s:
    if i not in s1:
        s1=s1+i
print(s1)
# (d) How do you count a number of vowels and consonants in a given string
s2='samayreddy'
vo='aeiouAEIOU'
vc=0
cc=0
for i in s2:
    if i in vo:
        vc+=1
    else:
        cc+=1
print(vc)
print(cc)
# (e) length of string. (diff methods)

# (f) String Reverse. (diff methods)
#
# 2. Write a program that asks the user to input n integers,
# and then prints the largest odd number that was entered.
# If no odd number was entered, it should print a message to that effect.
d1={1:'a',2:'b',3:'c'}
d2={4:'d',5:'e',6:'f',7:'g'}
d3={**d1,**d2}
d1.update(d2)
print(d1)
print(d3)
print(d1|d2)
