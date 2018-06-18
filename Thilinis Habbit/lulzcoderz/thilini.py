x = int(input())
for p in range(0,x):
    sumx = 0
    y = int(input())
    if(y %2 == 0):
        
        for q in range(1,y,2):
            sumx += q

        print(sumx)
    else:
        for q in range(1,(y+1),2):
            sumx += q

        print(sumx)
