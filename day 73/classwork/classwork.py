def number(bus_stops):
    return sum(stop[0] - stop[1] for stop in bus_stops)










def dont_give_me_five(start,end):
    count = 0
    for i in range(start, end +1):
        if '5' not in str(i):
            count += 1
    return count





def array_diff(a, b):
    result = []
    for item in a:
        if item not in b:
            result.append(item)
    return result







def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    north= walk.count("n")
    east = walk.count("e")
    south = walk.count("s")
    west = walk.count("w")
    
    if east == west and south == north:
        return True
    else:
        return False
    







def digital_root(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n