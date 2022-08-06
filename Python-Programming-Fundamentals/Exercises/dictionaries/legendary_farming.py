needed_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
got_desired_item = False
materials = input().split()
while True:
    for i in range(0, len(materials), 2):
        if materials[i + 1].lower() in needed_materials:
            needed_materials[materials[i + 1].lower()] += int(materials[i])
        else:
            if materials[i + 1].lower() not in junk:
                junk[materials[i + 1].lower()] = int(materials[i])
            else:
                junk[materials[i + 1].lower()] += int(materials[i])
        if needed_materials["shards"] >= 250:
            needed_materials["shards"] -= 250
            required_item = 'Shadowmourne'
            got_desired_item = True
        if needed_materials["fragments"] >= 250:
            needed_materials["fragments"] -= 250
            required_item = 'Valanyr'
            got_desired_item = True
        if needed_materials["motes"] >= 250:
            needed_materials["motes"] -= 250
            required_item = 'Dragonwrath'
            got_desired_item = True
        if got_desired_item:
            break
    if got_desired_item:
        print(f"{required_item} obtained!")
        break
    materials = input().split()

for key, value in needed_materials.items():
    print(f'{key}: {value}')
for key, value in junk.items():
    print(f'{key}: {value}')
