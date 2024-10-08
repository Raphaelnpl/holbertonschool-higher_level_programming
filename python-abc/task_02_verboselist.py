#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Iterable, SupportsIndex
'''module for class VerboseList'''


class VerboseList(list):
    '''class VerboseList that inherits from list'''
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item

