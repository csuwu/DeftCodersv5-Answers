y = int(input())

data=[]
for y in range(0, y):
    s = input()
    data.append(s)





for z in data:
    print(''.join(chr(int(z[i*8:i*8+8],2)) for i in range(len(z)//8)))
