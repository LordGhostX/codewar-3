def solution(args):
    number_map = {args[0][i]: i for i in range(len(args[0]))}
    for k in number_map:
        half_num = args[1] - k
        if number_map.get(half_num):
            first_index = number_map[k]
            second_index = number_map[half_num]
            return first_index, second_index
