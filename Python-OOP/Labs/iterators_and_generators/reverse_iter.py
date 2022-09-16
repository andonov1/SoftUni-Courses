class reverse_iter:
    def __init__(self, array):
        self.array = array
        self.start = len(array) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= 0:
            current = self.array[self.start]
            self.start -= 1
            return current
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
