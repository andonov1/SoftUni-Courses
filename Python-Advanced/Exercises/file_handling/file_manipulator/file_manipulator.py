import os

while True:
    command = input()
    if command == 'End':
        break
    command_parts = command.split('-')
    action = command_parts[0]
    file_name = command_parts[1]
    if action == 'Create':
        open(file_name, 'w').close()
    elif action == 'Add':
        content = command_parts[2]
        with open(file_name, 'a') as file:
            file.write(content + "\n")
    elif action == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
    elif action == 'Replace':
        old_string = command_parts[2]
        new_string = command_parts[3]
        if os.path.exists(file_name):
            with open(file_name, 'r+') as file:
                new_file_content = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(new_file_content)
        else:
            print("An error occurred")
