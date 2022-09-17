class sequence_repeat:
    def __init__(self, sequence, num):
        self.sequence = sequence
        self.num = num
        self.pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer == self.num:
            raise StopIteration
        symbol = self.sequence[self.pointer % len(self.sequence)]
        self.pointer += 1
        return symbol


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
