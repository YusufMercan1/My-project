def two_sum(tal, mål):
    tal_dict = {}
    for i, num in enumerate(tal):
        komplement = mål - num
        if komplement in tal_dict:
            return [tal_dict[komplement], i]
        tal_dict[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))