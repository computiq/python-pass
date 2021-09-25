"""
Instructions:

1. Create a class named ReversedString that inherits from StringOperations class
2. Implement the function reverse
3. reverse function should be a one liner function that returns the reverse string to_be_reversed
4. Instantiate the class ReversedString
5. Print to show your function implementation result
"""


class StringOperations:
    def reverse(to_be_reversed: str = None):
        return to_be_reversed[::-1]
    
class ReversedString(StringOperations):
    pass


reversedInput = ReversedString

print(reversedInput.reverse(input("Write your string : ")))
