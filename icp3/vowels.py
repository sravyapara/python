str=input("enter the string")
def vowel_count(str):
    # Intializing count  to 0
    count = 0
    # Creating a set of vowels
    vowel = {"a","e","i","o","u"}
    # to find the number of vowels
    for alphabet in str:
        # If alphabet is present then count is incremented
        if alphabet in vowel:
            count = count + 1
    print("No. of vowels :", count)
# Function Call
vowel_count(str)