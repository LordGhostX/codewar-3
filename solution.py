def solution(args):
    for i, j in enumerate(args[0]):
        for k, l in enumerate(args[0]):
            if j + l == args[1]:
                return i, k