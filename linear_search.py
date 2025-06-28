def linear(list, target):
    for i in list:
        for j in i:
            if j == target:
                return i

