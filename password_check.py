
correct_password='password'
name=input("Enter Name")
lastname=input("Enter last name")
password=input("Enter Your password\n")

# for password in correct_password:
#     print ("Match Found")
#     break

while password!=correct_password:
    password=input("Wrong password..Enter Your password again\n")
    print("Please enter correct password")
print("Hi %s %s You are logged in" %(name,lastname) )
