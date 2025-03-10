return " ".join(word[::-1] if len(word) >= 5 else word for word in sentence.split())




return int("".join(sorted(set(map(str, digits)))))





 days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days.get(num, "Wrong, please enter a number between 1 and 7")





def alphabetic(s):
    return s == ''.join(sorted(s))