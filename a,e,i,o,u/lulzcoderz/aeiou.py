s = input()
a = 0
e = 0
x = 0
o = 0
u = 0
for i in s:
    if(i=='a' or i=='A'):
        a = a+1
    elif(i=='e' or i=='E'):
        e = e+1
    elif(i=='i' or i=='I'):
        x = x+1
    elif(i=='o' or i=='O'):
        o = o +1
    elif(i=='U' or i=='u'):
        u = u+1
print("a -",a)
print("e -",e)
print("i -",x)
print("o -",o)
print("u -",u)
