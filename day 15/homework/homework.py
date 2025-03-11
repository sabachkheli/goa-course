
my_name = "saba"  
user_name = input("Enter your name: ")
if user_name == my_name:
    print("Hello")
else:
    print("Bye")


my_fav_number = 7  
user_fav_number = int(input("Enter your favorite number: "))

if user_fav_number == my_fav_number:
    print("Perfect")
elif user_fav_number > my_fav_number:
    print("More")
else:
    print("Less")


for i in range(150):
    if i % 2 == 0:
        print("Even", i)
    else:
        print("Odd", i)


user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

my_age = 25 

if user_name == my_name and user_age == my_age:
    print("Twins")
else:
    print("Not Twins")


correct_password = "password123" 
user_input = ""

while user_input != correct_password:
    user_input = input("Enter the password: ")

print("Access Granted!")
