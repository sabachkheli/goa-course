def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000


def find_needle(haystack):
    position = haystack.index("needle")
    return f"found the needle at position {position}"



def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result





def rental_car_cost(d):
    cost = d * 40
    if d >= 7:
        cost -= 50
    elif d >= 3:
        cost -= 20
    return cost





def is_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a





def stray(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num
        






def repeats(arr):
    return sum(x for x in arr if arr.count(x) == 1)