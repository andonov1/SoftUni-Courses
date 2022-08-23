nums = [int(s) for s in input().split()]

positive = sum([s for s in nums if s >= 0])
negative = sum([s for s in nums if s < 0])
print(negative)
print(positive)

if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")