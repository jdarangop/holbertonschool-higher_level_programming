#!/usr/bin/python3


class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        """Print a sorted list"""
        tmp = self.copy()
        print(sorted(tmp))
