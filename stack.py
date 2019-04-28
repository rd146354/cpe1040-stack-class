def expect_int(i, sample):
    if not isinstance(i, type(sample)):
        raise ValueError('Expected {}'.format(type(sample)) + ' but got {}'.format(type(i)))
    else:
        print('Got an {}'.format(type(sample)) + ' value {}'.format(i))


class Stack():
    def __init__(self):
        self.sample = 6
        print("New Stack object")
        self.value = list()

    def pop(self):
        print("Popping...")
        self.value = list()
        return None

    def push(self, value):
        expect_int(value, self.sample)
        print("Pushing...")
        self.value.append(value)
        return self.value

