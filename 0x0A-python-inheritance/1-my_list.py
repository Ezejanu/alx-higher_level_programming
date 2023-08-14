#!/usr/bin/python3
""" A child class (MyList) which inherits from the parent class (list) """


class MyList(list):

    """ The constructor for the class MyList """


    def print_sorted(self):
        """ A public instance to print the list """

        print(sorted(self))
