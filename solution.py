def solution(numbers, target):
    # generate a map of the numbers in the input
    # the values become the keys and the index become the values
    number_map = {numbers[i]: i for i in range(len(numbers))}

    # iterate through the keys in the number map
    for k in number_map:
        # to find a sum, check if the half sum is also a key in the map
        # runtime ~ O(n), where n = the length of the input array
        half_num = target - k
        if number_map.get(half_num):
            first_index = number_map[k]
            second_index = number_map[half_num]
            return first_index, second_index
