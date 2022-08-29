from os import walk

files_by_extent = {}
for root, dirs, files in walk('.'):
    for file in files:
        extension = file.split('.')[-1]
        if extension not in files_by_extent:
            files_by_extent[extension] = []
        files_by_extent[extension].append(file)

for extension, files in sorted(files_by_extent.items()):
    print(f'.{extension}')
    for file in files:
        print(f'--- {file}')
