vowels=['a','e','i','o','u'] #keep a list of vowels
rv=[0,0,0,0,0] #to store counts of each vowel
n=input("").lower() #convert input string to lower case
for i in n: #to loop through the input string n
    for j in range(0,len(vowels)): #check each character with vowels array
        if(i==vowels[j]): 
            rv[j]=rv[j]+1 #incerement relevant index of array if a character is in vowels array

for i in range(0,len(rv)): #to loop through arrays
    print(vowels[i],"-",rv[i]) #print expected output
