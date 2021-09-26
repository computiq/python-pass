class StringOperations:
    def reverse(self, *, to_be_reversed: str = None):
        raise NotImplemented('This method need to be implemented')

class ReversedString (StringOperations):
    def reverse(self, *, to_be_reversed: str = None):
        return to_be_reversed[::-1]

rev = ReversedString()
print(rev.reverse(to_be_reversed=input("enter some text: ")))
