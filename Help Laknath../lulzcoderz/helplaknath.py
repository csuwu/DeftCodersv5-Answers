x = int(input())
for p in range(0,x):
    lower = list(map(int,input().split(" ")))
    li=[]
    for num in range(lower[0],lower[1] + 1):
      if num > 1:
          for i in range(2,num):
              if (num % i) == 0:
                  break
          else:
              li.append(num)
    x = len(li)
    print(x)
