class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.result = tuple(self.dictionary.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dictionary):
            raise StopIteration()
        i = self.index
        self.index += 1
        return self.result[i]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)