class vowels:
    def __init__(self, string: str):
        self.string = string
        self.vowels = ["a", "e", "i", "o", "u", "y"]
        self.vowels_in_text = [char for char in self.string if char.lower() in self.vowels]
        self.start = 0
        self.end = len(self.vowels_in_text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration
        index = self.start
        self.start += 1
        return self.vowels_in_text[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
