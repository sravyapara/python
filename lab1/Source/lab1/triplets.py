#defining a function with 2 parameters
def triplets(A, arr_size):
    found=True
    # first element is A[i]
    for i in range(0, arr_size - 2):
        #  second element is A[j]
        for j in range(i + 1, arr_size - 1):
            # fixing the third number
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == 0: # if sum is 0 then print the triplets
                    print("Triplet is", "[(",A[i],",", A[j], ",", A[k],")]")
                    found= True
    if (found== False): #if no triplets then print not found
        print("not found")
#declaring a predefined list
A =[1, 3, 6, 2, -1, -2, 8, 9,0]
#the condition
arr_size = len(A)
triplets(A, arr_size)
