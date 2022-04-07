"""
Module for Homework 4, Problem 3
Author: Suneeta Ramaswami
Object Oriented Programming (50:198:113), Spring 2022

This module contains the Bag class implementaion.
"""

class Bag:
    """
    A container class to store unordered collection of items.
    """
    def __init__(self):
        """
        Constructor creates an empty bag
        """
        self.__contents = {}
    def insert(self, item):
        """
        Insert item into bag
        """
        self.__contents[item] = self.__contents.get(item, 0) + 1
    def erase_one(self, item):
        """
        Delete one occurrence of item from bag
        """
        if item in self.__contents:
            self.__contents[item] = self.__contents[item] - 1
            if self.__contents[item] == 0:
                del self.__contents[item]
    def count(self, item):
        """
        Return the count (number of occurrences) of
        item in bag
        """
        if item in self.__contents:
            return self.__contents[item]
        else:
            return 0
    def items(self):
        """
        Return a list of items in the bag
        """
        return list(self.__contents.keys())
    def __str__(self):
        """
        Return a printable representation of bag
        """
        bag_str = ""
        for item in self.__contents:
            for i in range(self.__contents[item]):
                bag_str = bag_str + str(item) + ' '
        return bag_str

