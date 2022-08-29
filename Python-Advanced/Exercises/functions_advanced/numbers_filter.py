def even_odd_filter(**kwargs):
    result_dict = {}
    for key, nums in kwargs.items():
        parity = 0 if key == 'even' else 1
        filtered = [x for x in nums if x % 2 == parity]
        result_dict[key] = filtered
    return dict(sorted(result_dict.items(), key=lambda kvpt: -len(kvpt[1])))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
