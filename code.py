class FlatIterator:
    def __init__(self, list_):
        self.list_ = list_
        self.list_index = -1
        self.result = []

    def __iter__(self):
        self.cursor = self.list_[0]
        return self

    def __next__(self):
        self.list_index+=1
        self.cursor = self.list_[self.list_index]
        for i in self.cursor:
            self.result.append(i)
        if self.cursor == self.list_[len(self.list_)-1]:
            raise StopIteration
        return self.result

nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
flat_list = [item for item in FlatIterator(nested_list)][0]
print(flat_list)