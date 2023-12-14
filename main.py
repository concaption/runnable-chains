class Runnable:
    """
    A class that represents a runnable function.
    """

    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        def chained(*args, **kwargs):
            return other(self.func(*args, **kwargs))
        return Runnable(chained)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

def add_five(x):
    return x + 5

def multiply_by_two(x):
    return x * 2

def square(x):
    return x * x

add_five = Runnable(add_five)
multiply_by_two = Runnable(multiply_by_two)
square = Runnable(square)

x = 5

# Using the Runnable class, we can chain functions together
print((add_five | multiply_by_two | square)(x))
# or
chain = add_five | multiply_by_two | square
print(chain(x))
# This is equivalent to:
print((square(multiply_by_two(add_five(5)))))
# Which is equivalent to:
print(((x + 5) * 2) ** 2)