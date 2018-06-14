Symbol =['$','@','#','!']
while True :
 passwcheck = input("Enter the password :")

#calculating the length of the entered password
 if len(passwcheck)< 6 :
    print("The length of the password should be at least 6 characters long")
    continue
 elif len(passwcheck)> 16 :
    print("The length of the password should be not be greater than 16")
    continue

 #checking for any numbers in the password entered using isdigit()
 elif not any(char.isdigit() for char in passwcheck):
    print('The password should have at least one number')
    continue
 #check if the password entered has any uppercase letters
 elif not any(char.isupper() for char in passwcheck):
    print('The password should have at least one uppercase letter')
    continue
 #check if the password entered has any lowercase letters
 elif not any(char.islower() for char in passwcheck):
    print('The password should have at least one lowercase letter')
    continue
 #checking for any of special characters from the list declared
 elif not any(char in Symbol for char in passwcheck):
    print('The password should have at least one of the symbols $@#!')
    continue
 #if password meets all the conditions then loop stops
 else :
    print("Password entered is correct")
    print(passwcheck)
    break