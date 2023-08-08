#!/usr/bin/python3

""" This is a class that defines a rectangle """


class Rectangle:
    """ This is a class that defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            row = ""
            # Reset row for each new row of the rectangle
            for j in range(self.__width):
                row += Rectangle.print_symbol
            rectangle_str += row
            if i != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def get_number_of_instances(cls):
        return cls.number_of_instances

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance (rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance (rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_rect_1 = rect_1.area()
        area_rect_2 = rect_2.area()

        if area_rect_1 >= area_rect_2:
            return rect_1
        else:
            return rect_2
