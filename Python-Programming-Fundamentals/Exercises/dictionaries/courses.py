courses = {}
command = input()

while command != 'end':
    course, student = command.split(' : ')
    if course not in courses:
        courses[course] = [student]
    else:
        courses[course] += [student]
    command = input()
for key in courses:
    print(f"{key}: {len(courses[key])}")
    for name in courses[key]:
        print(f"-- {name}")