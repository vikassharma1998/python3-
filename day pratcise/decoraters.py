def decorator(func):
    def value(a, b):
        print(f"your value is {a} and {b}")
        func(a, b)
    return value


@decorator
def add(a, b):
    print(f"your add result is :", a + b)


def sub(a, b):
    print(f"your subtract result is :", a - b)


add(2, 4)

sub(5, 4)
