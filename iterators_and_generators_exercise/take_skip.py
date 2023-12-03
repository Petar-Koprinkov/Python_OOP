class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.number = - self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration()
        self.count -= 1
        self.number += self.step
        return self.number


numbers = take_skip(2, 6)

for number in numbers:
    print(number)