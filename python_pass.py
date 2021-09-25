class StringOperations:
    def reverse(self, *, to_be_reversed: str = None):
        raise NotImplemented('This method need to be implemented')
    def __init__(self, to_be_reversed):
        self.str = to_be_reversed

    def reverse(self):
        return self.str[::-1]

class ReversedString(StringOperations):
    pass

if __name__ == "__main__":
    reversedname = ReversedString("hussain alyasiry")
    print(reversedname.reverse())
