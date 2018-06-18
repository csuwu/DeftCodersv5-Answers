string=input()
char=0
word=1
if string=="":
    print("invalid")
else:
    for i in string:
      char=char+1
      if(i==' '):
            word=word+1
      if (string==0):
          print(error)
    print(word)
