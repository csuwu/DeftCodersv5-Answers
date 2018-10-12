x = input()
result = ''.join(c for c in x if c.isalpha())
if(len(result)>20):
    print("error")
else:
    
    print(result)
