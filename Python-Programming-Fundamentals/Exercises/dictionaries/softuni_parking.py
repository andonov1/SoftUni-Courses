num_of_commands = int(input())
register_dict = {}
for i in range(num_of_commands):
    data = input().split()
    action = data[0]
    name = data[1]
    if action == 'register':
        license_num = data[2]
        if name not in register_dict:
            register_dict[name] = license_num
            print(f"{name} registered {license_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {register_dict[name]}")
    else:
        if name not in register_dict:
            print(f"ERROR: user {name} not found")
        else:
            register_dict.pop(name)
            print(f'{name} unregistered successfully')
for key, value in register_dict.items():
    print(f"{key} => {value}")