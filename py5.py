# 3.Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)
for k,v in dict1.items():
    dict2[k] = v
print(dict(sorted(dict2.items(),key=lambda item: item[1])))