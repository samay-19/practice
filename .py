# 5)create a dictionary based on list of keys and add value as 100 for all keys.
# ex: I/p a = [1,2,4,5]
# o/p b = {1:100,2:100,4:100,5:100}
#
#
# l=[1,2,3,4,5]
# d={}
# for i in l:
#     d[i]=100
# print(d)
# # or
# d1=dict(map(lambda x:(x, 100), l))
# print(d1)

# (d) How do you count a number of vowels and consonants in a given string
s='samay'
v='aeiouAEIOU'
c=0
vc1,cc2=0,0
for i in s:
    if i in v:
        vc1+=1
    else:
        cc2+=1
print(vc1)
print(cc2)
# (e) length of string. (diff methods)
for i in s:
    c+=1
print(c)
# (f) String Reverse. (diff methods)

s='hhhsamay is greek is god godhhh'
print(s[::-1])
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.find('greek'))
print(s.count('god'))
print(s.replace('samay','harshith'))
print(s.split())
print(s.strip())
print('-'.join(s.split()))
print("".join(list(reversed(s))))
s1='hello world 123'
for i in s1:
    if i.isalpha():
        print(i,end=" ")
print()
print(ord('a'))
print(chr(64))
