class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.result = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.result > self.number:
            raise StopIteration()
        else:
            self.result += 1
            i = self.index
            self.index += 1
            if i == len(self.sequence):
                self.index = 0
                i = self.index
                self.index += 1
            return self.sequence[i]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
