from itertools import combinations
new_list=[]
print_list=[]
# A list is created using combinations function with each combination length set to 3
new_list=list(combinations([1,3,6,2,-1,2,8,-2,9], 3))
var1=len(new_list)
j=0
# To check whether the triplet sum is equal to zero
for i in range(var1):
    if(sum(new_list[j])==0):
        print_list.append(new_list[j])
    j=j+1
# Print all the triplets whose sum is equal to zero
print(print_list)
