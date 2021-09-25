"""
Instructions:

1. Create a class named ReversedString that inherits from StringOperations class
2. Implement the function reverse
3. reverse function should be a one liner function that returns the reverse string to_be_reversed
4. Instantiate the class ReversedString
5. Print to show your function implementation result
"""




"""
* Noaman Monther Mahmood
* YANHAD Coding Bootcamp (Tasks - 1)
* Python Side 
* Use Better Comments {for better experiance with this task solution}
* https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments

"""


class StringOperations:
    def reverse(self, to_be_reversed: str = None): return to_be_reversed[::-1]
        # * returning the reversed value of passed text
        # ! reverse function should be a one liner function that returns the reverse string to_be_reversed
       
        # raise NotImplemented('This method need to be implemented')
class ReversedString(StringOperations):
    pass # ! we want to implement it later


# * here we are going to Instantiate the class ReversedString
reversedString=ReversedString()


print( reversedString.reverse('Computiq'))