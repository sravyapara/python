web = ['sravya', 'vineeth','hema','Amulya']
python = ['sravya', 'vineeth', 'sunny','priyanka']

#calculating the length which gives the number of people
first = len(web)
sec = len(python)
x = 0
sameclass = [] #creating empty lists
diffclass = []

#comparing each student from web to python one by one
for i in range(first):
    if web[x] in python:
        sameclass.append(web[x]) # if found in python then append to same course
    else:
        diffclass.append(web[x]) #else append to disscourse
    x = x + 1 #increment x
y = 0
for j in range(sec): # comparing students from python to web
    if python[y] not in web:
        diffclass.append(python[y])
    y = y + 1
print("sameclass",sameclass)
print("diffclass",diffclass)