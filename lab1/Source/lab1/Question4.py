
f={"vineeth", "vinay", "kranthi", "bhavesh"} # First list
s={"kranthi", "bhavesh", "yuvesh"} # Second list
# An empty list stores the common elements present in both the list
common_elements=[]
uncommon_elements=[]

for i in f:
    # checking if each element of first list exists in second list
    if i in s:
        #if so add it in common elements list
        common_elements.append(i)
print("common elememts are", common_elements)
a= f.symmetric_difference(s)
print("Uncommon elements are", a)




