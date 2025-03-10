def filter_list(l):
    return [item for item in l if isinstance(item, int)]

def to_jaden_case(string):
    list=string.split()
    new_list=[i.capitalize()for i in the list]
    print(new_list)
    return " ".join


def sum_mix(arr):
    return sum(int(i) for i in arr)


def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)



def reverse_words(s):
    return ' '.join(s.split()[::-1])