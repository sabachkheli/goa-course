def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split()]


def get_size(w,h,d):
    area = 2 * (d * w + w * h + h * d)
    volume = d * w * h
    return [area, volume]


def maps(a):
    return [x * 2 for x in a]



def greet():
    return "hello world!"


def opposite(number):
    return -number