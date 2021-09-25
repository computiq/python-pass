"""
Instructions:

1. Create a class named ReversedString that inherits from StringOperations class
2. Implement the function reverse
3. reverse function should be a one liner function that returns the reverse string to_be_reversed
4. Instantiate the class ReversedString
5. Print to show your function implementation result
"""


class StringOperations:
    def reverse(self, to_be_reversed):

        string_leangh = len(to_be_reversed)

        

        reversed_string  =  to_be_reversed

        reversed_string = reversed_string[::-1]
        return reversed_string

            
            

class ReversedString(StringOperations):
    pass

string_to_revers = ReversedString()

print(string_to_revers.reverse("hello world "))