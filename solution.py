def solution(array_of_integers, integer):
    for i, j in enumerate(array_of_integers):
        for k, l in enumerate(array_of_integers):
            if j + l == integer:
                return i, k