def is_rotated(s,k):
    a=""
    for i in s:
        if i.islower():
            z=ord(i)+k
            if z>122:
                z=z-26
            elif z<97:
                z=z+26
            a+=chr(z)
        elif i.isupper():
            z=ord(i)+k
            if z>90:
                z=z-26
            elif z<65:
                z=z+26
            a+=chr(z)
    return a

n1='zebra'
n2=1
l=is_rotated(n1,n2)
print(l)

