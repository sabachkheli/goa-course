def format_money(amount):
    amount_str = str(amount)
    if '.' not in amount_str:
        amount_str += '.00'
    elif len(amount_str.split('.')[1]) == 1:
        amount_str += '0'
    return '$' + amount_str

def swap_values(args): 
    args.reverse()


def sum_mul(n, m):


 def multiples_of_index(arr):
-return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]
