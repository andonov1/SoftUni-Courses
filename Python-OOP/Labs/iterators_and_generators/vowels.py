class vowels():
    def __init__(self, text):
        self.text = text
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= len(self.text) - 1:
            current_char = self.text[self.i]
            self.i += 1
            if current_char in 'AEIOUYaeiouy':
                return current_char
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
