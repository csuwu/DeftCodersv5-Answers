import re

x = int(input())
li = []
for p in range(0,x):
    y = input()
    match = re.match(r'[a-zA-z0-9\-_]+@[a-zA-Z0-9]+\..{1,3}$', y)
    if match:
        li.append(y)
li.sort(key=str.lower)
for q in range(0,(len(li)-1)):
    print(li[q],end=",")
print(li[-1])
