from stack import Stack


def test_integers():
    s = Stack()
    s.push(int(5))
    print(s.value)
    t = s.pop()
    print(s.value)
    print(t)


def test_floats():
    s = Stack()
    s.push(3.14159)
    print(s.value)
    t = s.pop()
    print(s.value)
    print(t)


def test_strings():
    s = Stack()
    s.push('alchemy')
    print(s.value)
    t = s.pop()
    print(s.value)
    print(t)


def test_all():
    s = Stack()
    s.push(5)
    s.push(3.14159)
    s.push('alchemy')
    print(s.value)
    t = s.pop()
    print(t)


if __name__ == '__main__':
    test_integers()
    test_floats()
    test_strings()
    test_all()
