string = string.lower()
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True








result = [ch.upper() + ch.lower() * i for i, ch in enumerate(st)]
    return '-'.join(result)





 return len(pin) in [4, 6] and pin.isdigit()



 return n ** 3