file_string = input().split('\\')

file_name, file_extension = file_string[-1].split('.')
print(f'File name: {file_name}\n'
      f'File extension: {file_extension}')