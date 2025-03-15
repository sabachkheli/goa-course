car_description = {
    "brand": "porche",
    "model": "911 gt3 rs",
    "year": 2022
}


for key, value in car_description.items():
    print(f"{key}: {value}")


keys = car_description.keys()
values = car_description.values()

print("Keys:", list(keys))
print("Values:", list(values))





set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


union_set = set1.union(set2)
print("გაერთიანებული სეტი:", union_set)


intersection_set = set1.intersection(set2)
print("მსგავსება:", intersection_set)


difference_set1 = set1.difference(set2)
print("მხოლოდ set1-ის ელემენტები:", difference_set1)


difference_set2 = set2.difference(set1)
print("მხოლოდ set2-ის ელემენტები:", difference_set2)







car_info = {
    "brand": "BMW",
    "model": "M5",
    "year": 2023
}


for value in car_info.values():
    print(value)




#dictionary არის მონაცემტა სტრუკტურა რომელშიც  გასაღები და მნიიშვნელობაა შენახული




user_info = {
    "fullname": "playboycarti",
    "birth_year": 1995,
    "country": "atlanta georgia united states"
}


combined_list = []


for key, value in user_info.items():
    combined_list.extend([key, value])  


print(combined_list)


profile_info = {
    "username": "album",
    "email": "albumdropped@gmail.com",
    "location": "tweeter"
}


key_input = input("Enter a new key: ")
value_input = input("Enter the value: ")


if key_input in profile_info:
    print("Error: This key already exists. Try again!")
else:
    profile_info[key_input] = value_input
    print("Success! New data has been added.")


print("Updated profile:", profile_info)
