# List (სიამ) არის ნივთების გროვა, რომელიც შეიძლება შეიცავდეს დუბლიკატებს და რომელშიც ელემენტებს აქვთ ინდექსები.
# Set (მგრძნობიარე მასივი) არის უნიკალური ნივთების გროვა, სადაც არ არის დუპლიკატები. 

numbers = {1, 2, 3, 4}
# ინდექსინგის საშუალებით შეცვლა არ შეიძლeba
numbers[0] = 5  # გამოიწვევს შეცდომას, რადგან set არ აქვს ინდექსები

fast_food = {"burger", "pizza", "fries", "soda"}
print(f"Fast food items: {fast_food}")


fast_food.clear()


healthy_food = {"salad", "apple", "banana", "carrot"}
fast_food.update(healthy_food)

print(f"Healthy food items: {fast_food}")

Fast_food_items: {'pizza', 'burger', 'fries', 'soda'}
Healthy_food_items: {'salad', 'apple', 'banana', 'carrot'}

def remove_duplicates(input_list):
    return list(set(input_list))

# Test cases
list1 = [7, 5, 44, 14, 5, 5, 44]
list2 = [89, 90, 56, 45, 90, 78, 90]

print(remove_duplicates(list1))  # Output: [5, 7, 44, 14]
print(remove_duplicates(list2))  # Output: [89, 90, 56, 45, 78] 






