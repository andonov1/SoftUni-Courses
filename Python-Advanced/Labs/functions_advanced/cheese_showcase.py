def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for cheese, values in sorted_cheeses:
        result += cheese + '\n'
        result += "\n".join([str(s) for s in sorted(values, reverse=True)]) + '\n'
    return result


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

