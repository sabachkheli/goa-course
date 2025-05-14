count = 0
    for i in range(start, end +1):
        if '5' not in str(i):
            count += 1
    return count





 if n <= 0:
        return 0
    return n * (n + 1) // 2





 if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return "no"