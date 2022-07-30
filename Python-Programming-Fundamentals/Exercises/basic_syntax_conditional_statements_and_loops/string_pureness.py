n = int(input())
for i in range(n):
    given_string = input()
    if "," in given_string or "." in given_string or "_" in given_string:
        print(f"{given_string} is not pure!")
    else:
        print(f"{given_string} is pure.")