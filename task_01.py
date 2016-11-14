#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """A simple function with exception handling.
        Args:
            var1(any): any type
            var2(any): any type
        Return:
            var1[var2]: when attempts to access any index or key of var1 exist
            var1 with a warning message: when attempts to access any index or key
            of var1 doesn't exist.
        Examples:
            >>> simple_lookup([1, 2], 4)
            Warning: Your index/key doesn't exist.
            [1, 2]
    """
    try:
        var1[var2]
    except(IndexError, KeyError):
        print "Warning: Your index/key doesn't exist."
        
        return var1
