from itertools import combinations


def solution(args):
    for number_set in combinations(args[0], 2):
        if sum(number_set) == args[1]:
            first_index = args[0].index(number_set[0])
            second_index = args[0].index(number_set[1])
            return first_index, second_index
