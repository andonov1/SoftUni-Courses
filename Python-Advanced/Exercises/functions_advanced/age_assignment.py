def age_assignment(*args, **kwargs):
    name_age_dict = {}
    result = []
    for name in sorted(args):
        name_age_dict[name] = kwargs[name[0]]
    for name, age in name_age_dict.items():
        result.append(f"{name} is {age} years old.")
    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
