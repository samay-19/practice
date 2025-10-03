# Write a Python function to flatten a nested list.
# flatten([1, [2, [3, 4], 5], 6]) o/p: [1, 2, 3, 4, 5, 6]
# from inspect import stack


# def flatten(lst):
#     l=[]
#     for i in lst:
#         if isinstance(i,list):
#             l.extend(flatten(i))
#         else:
#             l.append(i)
#     return l
# n=[1, [2, [3, 4], 5], 6]
# print(flatten(n))
# Write a Python function to check if a string has balanced parentheses
# , brackets, and braces.
# is_balanced("({[]})") o/p: True
# is_balanced("([)]")   o/p: False
# is_balanced("{[()]}") o/p: True
# is_balanced("{[(])}") o/p: False
# def is_balanced(s):
    # stack1= []
    # matching = {')': '(', ']': '[', '}': '{'}
    # for i in s:
    #     if iin matching.values():
    #         stack1.append(i)
    #     elif i in matching:
    #         if not stack or stack1[-1] != matching[i]:
    #             return False
    #         stack1.pop()
    # return not stack1


# Test cases
# print(is_balanced("({[]})"))  # True
# print(is_balanced("([)]"))  # False
# print(is_balanced("{[()]}"))  # True
# print(is_balanced("{[(])}"))  # False

d={'(' : ')' , '[' : ']' , '{' : '}' }
s="({}[{}])"
n= len(s)
z=0
i=0
j=n-1
if n%2 != 0:
	print(False)
else:
	while i<j:
		if d[s[i]] == s[j]:
			i+=1
			j-=1
		else:
			z=1
			break
	if z==0:
		print("True")
	else:
		print ("False")



















