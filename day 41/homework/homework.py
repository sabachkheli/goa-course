def sum_of_positives(arr):
    return sum(x for x in arr if x > 0)


def no_space(x):
    return x.replace(" ", "")

def century(year):
    return (year + 99) // 100

def maps(a):
    return [x * 2 for x in a]


def dna_to_rna(dna):
    return dna.replace('T', 'U')