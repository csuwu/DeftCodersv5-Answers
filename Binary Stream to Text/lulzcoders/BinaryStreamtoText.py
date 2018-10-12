n = int(input())
for p in range (0,n):
        txt = input()
        length=8
        x =[txt[i:i+length] for i in range(0, len(txt), length)]
        for i in range(0,len(x)):
            if(len(x[i]) == 8):
                print(chr(int(x[i][:8], 2)),end='')
        print()
