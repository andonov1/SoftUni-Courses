def start_spring(**kwargs):
    objects = {}
    result = ''
    for object, value in kwargs.items():
        if value not in objects:
            objects[value] = []
        objects[value].append(object)
    sorted_objects = {k: v for k, v in sorted(objects.items(), key=lambda x: (-len(x[1]), x[0]))}

    for type, obj in sorted_objects.items():
        result += f'{type}:\n'
        for object in sorted(obj):
            result += f'-{object}\n'

    return result


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
