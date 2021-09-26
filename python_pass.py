"""

1. Created a class named ReversedString that inherits from StringOperations class
2. Implemented the function reverse
3. reverse function is a one liner function that returns the reverse string to_be_reversed
4. Instantiated the class ReversedString
5. Printed to show the function implementation result
"""

class StringOperations:
    def reverse(self, *, to_be_reversed: str = None):
        raise NotImplemented('This method need to be implemented')

class ReversedString(StringOperations):
    def reverse(self, *, to_be_reversed: str = None):
        return to_be_reversed[::-1]
Instant=ReversedString();
string = "computiq python-pass"
print ("The original string  is : ",end="")
print (string)
  
print ("The reversed string is : ",end="")
print (Instant.reverse(to_be_reversed=string));
