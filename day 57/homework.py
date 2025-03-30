def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    





def count_by(x, n):
    return [x * i for i in range(1, n + 1)]










def abbrev_name(name):
    first, last = name.split()  # Split the name into first and last
    return f"{first[0].upper()}.{last[0].upper()}"  # Return initials with a dot












def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)










