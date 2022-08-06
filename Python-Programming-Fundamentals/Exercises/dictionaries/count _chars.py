text = "".join(input().split())
letters_cnt_dict = {}
for i in text:
    if i not in letters_cnt_dict:
        letters_cnt_dict[i] = 0
    letters_cnt_dict[i] += 1
for key, element in letters_cnt_dict.items():
    print(f'{key} -> {element}')