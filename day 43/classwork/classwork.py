def nth_even(n):
    return 2 * (n - 1);



def add_length(str_):
    return ["{} {}".format(word, len(word)) for word in str_.split()]


def array(string):
    parts = string.split(",")

    if len(parts) <= 2:
        return None

    return " ".join(parts[1:-1])