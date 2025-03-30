def distinct(seq):
    result = []
    for num in seq:
        if num not in result:
            result.append(num)
    return result



def get_planet_name(id):
    if id == 1:
        return "Mercury"
    elif id == 2:
        return "Venus"
    elif id == 3:
        return "Earth"
    elif id == 4:
        return "Mars"
    elif id == 5:
        return "Jupiter"
    elif id == 6:
        return "Saturn"
    elif id == 7:
        return "Uranus"
    elif id == 8:
        return "Neptune"
    else:
        return id
    



    def switch_it_up(number):
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return words[number]






def unusual_five():
    return len(["", "", "", "", ""])