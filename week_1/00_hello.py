input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    max = -1
    for num in array:
        if num > max:
            max = num
    return max


result = find_max_num(input)
print(result)