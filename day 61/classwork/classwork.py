return sum(marks) // len(marks)



 total = 0
    for game in games:
        x, y = map(int, game.split(':'))
        if x > y:
            total += 3
        elif x == y:
            total += 1
    return total







numbers.sort()
    return numbers[0] + numbers[1]




 return sum(stop[0] - stop[1] for stop in bus_stops)








if number < 0:
        return 0
    
    total_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    
    return total_sum




 for num in seq:
        if seq.count(num) % 2 != 0:
            return num