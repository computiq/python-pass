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
        #a copy from input named reversed_string
        reversed_string  =  to_be_reversed

        #reversing the copy by create a slice that starts with the length of the string, and ends at index 0
        reversed_string = reversed_string[::-1]
        
        #return a reversed copy
        return reversed_string

            
            
#create a ReversedString class inherting from String operation class
class ReversedString(StringOperations):
    pass

#creat an Instantiate from ReversedString class
string_to_revers = ReversedString()

#print the output of the reverse function
print(string_to_revers.reverse("hello world "))
