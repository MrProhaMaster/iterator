class FlatIterator:
    def __init__(self, list_):
        self.list_ = list_

    def __iter__(self):
        self.cursor = self.list_[0]
        return self

    def __next__(self):
        self.cursor = self.list_[self.list_.index(self.cursor)+1]

        if self.cursor == self.list_[len(self.list_)-1]:
            raise StopIteration
        return self.cursor

nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
for item in FlatIterator(nested_list):
	print(item)