count = 1

while count <= 20:
    print("hello world!")
    count += 1  





user_input = input("მოაწერეთ ელემენტები სიის სახით, გამიჯნული ცალსახად კომით: ")

my_list = user_input.split(", ")

for item in my_list:
    print(item)








my_set = {1, 2, 3, 4, 5}
my_set.add(6)  
print(my_set)  






my_dict = {"name": "Saba", "age": 13}
my_dict["city"] = "Tbilisi"  
print(my_dict)  



my_tuple = (1, 2, 3, 4)

print(my_tuple)  





print(5 > 3 and 8 < 10) 



print(5 > 10 and 8 < 10)  





print(5 > 10 and 8 > 10)  






name = "Saba"
print(name == "Saba" and len(name) > 3)  




a = 5
b = 10
print(a == 5 and b == 10)  





