box_of_clothes = [int(s) for s in input().split()]
default_rack_capacity = int(input())
current_rack_capacity = default_rack_capacity
racks_cnt = 1

while box_of_clothes:
    current_cloth = box_of_clothes.pop()
    if current_cloth <= current_rack_capacity:
        current_rack_capacity -= current_cloth
    else:
        racks_cnt += 1
        current_rack_capacity = default_rack_capacity
        current_rack_capacity -= current_cloth

print(racks_cnt)

