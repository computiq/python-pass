"""
Instructions:

1. Create a class named ReversedString that inherits from StringOperations class
2. Implement the function reverse
3. reverse function should be a one liner function that returns the reverse string to_be_reversed
4. Instantiate the class ReversedString
5. Print to show your function implementation result
"""


class StringOperations:

    def reverse(self, *, to_be_reversed: str = None):
        try:
            return to_be_reversed[:: -1]
        except TypeError:
            print("There is no String to be reversed")
            quit()


class ReversedString(StringOperations):

    # I can solve the problem by using constructor also
    # def __init__(self, to_be_reversed):
    #     self.to_be_reversed = to_be_reversed
    pass


# my_phrase = ReversedString( 'Hi How Are you') ##when using constructor
my_phrase = ReversedString()
print(my_phrase.reverse(to_be_reversed='Hello YANHAD'))
