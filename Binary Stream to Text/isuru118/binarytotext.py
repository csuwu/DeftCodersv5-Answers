import binascii #we need python binascii library for this easy question
x=int(input("")) #get the number of lines that will be given to read
for i in range(0,x): #loop for the given number of lines
    n=input("")
    if not(len(n)%8==0): #check for any invalid stream (we need to read exactly 8 bits for each output character)
        n=n[0:(len(n)-(len(n)%8))] #remove the additional characters
    n = int(n, 2) #convert input to an int of base 2 (binary)
    n=binascii.unhexlify('%x' % n).decode("utf-8") #convert each of the values stored in n , to utf-8
    print(n) #print output string (utf-8 decodedd value)
