class ListDecorator(list):

    def __init__(self, lst):
        self.__lst = lst

    def __len__(self):
        return len(self.__lst)

    def __getitem__(self, index):
        return self.__lst[index]

    def __setitem__(self, index, value):
        self.__lst[index] = value

    def __str__(self):
        return str(self.__lst)

    def swap(self, i, j):
        """Swap elements at indices i and j."""
        temp = self.__lst[i]
        self.__lst[i] = self.__lst[j]
        self.__lst[j] = temp
