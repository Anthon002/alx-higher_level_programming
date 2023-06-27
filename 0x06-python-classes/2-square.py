class Square:
    def __init__(self, size=0):
        self.__size = 0
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
