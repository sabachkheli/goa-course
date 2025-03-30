def format_money(amount):
    amount_str = str(amount)
    if '.' not in amount_str:
        amount_str += '.00'
    elif len(amount_str.split('.')[1]) == 1:
        amount_str += '0'
    return '$' + amount_str










def swap_values(args): 
    args.reverse()







def same_case(a, b): 
    if not (a.isalpha() and b.isalpha()): 
        return -1
    if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
        return 1
    else:
        return 0
    







def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    return sum(i for i in range(n, m, n))










def multiple_of_index(arr):
    return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]








def calculate_age(year_of_birth, current_year):
    age_difference = current_year - year_of_birth
    
    if age_difference > 0:
        return f"You are {age_difference} year{'s' if age_difference > 1 else ''} old."
    elif age_difference < 0:
        return f"You will be born in {-age_difference} year{'s' if -age_difference > 1 else ''}."
    else:
        return "You were born this very year!"
