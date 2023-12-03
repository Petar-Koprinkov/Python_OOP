from itertools import permutations


def possible_permutations(input_list):
    for perm in permutations(input_list):
        yield list(perm)


my_list = [1, 2, 3]
for perm in possible_permutations(my_list):
    print(perm)