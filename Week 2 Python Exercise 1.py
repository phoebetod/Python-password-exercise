#Exercise 1: asking for a password
#Step 1 - ask user to input a password.

password = input("Please enter your new password")

#Step 2 - ask user to re-enter password

password2 = input("Please enter your password again")

#Step 3 - check that the passwords are the same before continuing

if password != password2:
    print("Your passwords don't match")

while password != password2:
    password2 = input("Please enter your password again, it must match your first password")

#Step 3 - Use length of password as parameter for strength of password. First need to determine the length of the password, which is a string.

i = 0
for x in password:
    i = i + 1 
    
#Step 4 - Use the parameter that a password less than 5 letters is weak, between 5 and 7 letters is medium, greater than 8 letters is strong. Use if statements to determine which bracket the password (string) sits in. Return feedback to the user about the strength of their password.

if i < 5:
    print("Your password is weak")

if i >= 5 and i < 8:
    print("Your password is of medium strength")

if i >= 8:
    print("Your password is strong")








#for i in range(3, 10):
    #print(i)

#dogs = ["dalmation", "labrador", "alsatian", "beagle"]
#index = [   0          1           2          3   ]
#x = dogs[1]
#print(x)
#print(dogs)
#for dog in dogs:
#    print(dog)
#    if dog == "poodle":
#       break
#    else:
#        continue