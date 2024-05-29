class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("width must be a positive integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("height must be a positive integer")
        self.__height = value

class Square(Rectangle):
    def __init__(self, size=0):
        if isinstance(size, list):
            raise TypeError("size must be an integer")
        if not isinstance(size, int) or size < 0:
            raise ValueError("size must be a non-negative integer")
        super().__init__(size, size)
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("size must be a non-negative integer")
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

# Test cases
try:
    s = Square(781)
    print(s)
except Exception as e:
    print(e)

try:
    s = Square(4)
    print(s)
except Exception as e:
    print(e)

try:
    s = Square(5)
    print(s)
except Exception as e:
    print(e)

try:
    s = Square()
    s = Square([12, 52])
except Exception as e:
    print(e)

try:
    s = Square(-35)
except Exception as e:
    print(e)

try:
    s = Square(0)
    print(s)
except Exception as e:
    print(e)

try:
    s = Square(5)
    print(s.width)
    print(s.height)
except Exception as e:
    print(e)
