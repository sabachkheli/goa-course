my_dict = {
    "სახელი": "საბა",
    "ასაკი": 13,
    "ქალაქი": "თბილისი"
}


keys_list = []
values_list = []


for key, value in my_dict.items():
    keys_list.append(key)
    values_list.append(value)


print("Keys:", keys_list)
print("Values:", values_list)




result = [10, 43, 12, 11, 94, 10, 55, 7, 11]


unique_result = list(set(result))


print(unique_result)



person = {
    "სახელი": "საბა",
    "ასაკი": 12,
    "ქალაქი": "თბილისი"
}
print(person)



country = {
    "ქვეყანა": "საქართველო",
    "დედაქალაქი": "თბილისი",
    
}
print(country)




my_dict = {}


key = input("შეიყვანეთ საკვანძო სიტყვა: ")
meaning = input("შეიყვანეთ მნიშვნელობა: ")


my_dict[key] = meaning


new_meaning = input(f"შეიყვანეთ ახალი მნიშვნელობა საკვანძო სიტყვისთვის '{key}': ")


my_dict[key] = new_meaning


print( my_dict)


def remove_duplicates(lst):
    unique_list = []  
    for item in lst:
        if unique_list.count(item) == 0:
            unique_list.append(item)
    return unique_list  


numbers = [10, 43, 12, 11, 94, 10, 55, 7, 11]
print(remove_duplicates(numbers)) 




