# 1)write a program to get two lists from user and convert it into the dictionary.
keys=list(map(int,input("enter keys").split()))
values=input("enter values").split()
dic={}
for i in range(len(keys)):
    dic[keys[i]]=values[i]
print(dic)
