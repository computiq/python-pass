"""
Instructions:

1. Create a class named ReversedString that inherits from StringOperations class
2. Implement the function reverse
3. reverse function should be a one liner function that returns the reverse string to_be_reversed
4. Instantiate the class ReversedString
5. Print to show your function implementation result
"""


class StringOperations:
    def __init__(self, to_be_reversed):
        self.str = to_be_reversed

    def reverse(self):
        return self.str[-1: : -1]

class ReversedString(StringOperations):
    pass
        
if __name__ == "__main__":
    rs = ReversedString("Ali")
    print('Reversed String=', rs.reverse())
