#enter the input string
line1=str(input("enter the string"))
#creating an empty dictionary
dictionary={}
#splitting and sorting the words
splitw = sorted(line1.split())

for word in splitw:
    #if word is already present in dictionary then value is incremented by 1 else 1 is assigned to that word
    if word in dictionary:
        dictionary[word]+=1
    else:
        dictionary[word]=1
print(dictionary)




