class FlatIterator:
    def __init__(self, list_):
        self.list_ = list_
        self.list_index = 0
        self.in_list_index = -1
        self.result = []

    def __iter__(self):
        self.cursor = self.list_[self.list_index]
        return self

    def __next__(self):
        self.in_list_index+=1
        if self.in_list_index == len(self.list_[self.list_index]):
            self.in_list_index = 0
            self.list_index += 1
        if self.list_index == len(self.list_):
            raise StopIteration
        return self.list_[self.list_index][self.in_list_index]




nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
for item in FlatIterator(nested_list):
    print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)