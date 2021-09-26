"""
Instructions:

1. Create a class named ReversedString that inherits from StringOperations class
2. Implement the function reverse
3. reverse function should be a one liner function that returns the reverse string to_be_reversed
4. Instantiate the class ReversedString
5. Print to show your function implementation result
"""


class StringOperations:
    def reverse(self , * , to_be_reversed: str = None):
        raise NotImplemented("This method need to be implemented")


class ReversedString(StringOperations):

    def reverse(self , to_be_reversed:  str =None):
        word = ' '
        for i in to_be_reversed:
            word = i+word
        return word

string = ReversedString()
word='Programming'
print(string.reverse(word))
