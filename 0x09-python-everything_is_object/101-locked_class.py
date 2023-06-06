#!/usr/bin/python3
class :
    __slots__ = ('first_name')

    def __setattr__(self, name, value):
        if hasattr(self, name):
            super().__setattr__(name, value)
