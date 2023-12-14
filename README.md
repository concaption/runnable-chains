# Runnable Class in Python

This project demonstrates a powerful way to chain functions together using a class called [`Runnable`](main.py).

This project was inspired by runnables in LangChain Expression Language (LCEL).

## Overview

The [`Runnable`](main.py) class is defined in [`main.py`](main.py). It represents a function that can be run, and it provides a mechanism to chain multiple functions together using the bitwise OR operator (`|`).

## Usage

Here's an example of how to use the [`Runnable`](main.py) class:

```python
from main import Runnable

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
```

In this example, we first define three functions: [`add_five`](main.py), [`multiply_by_two`](main.py), and [`square`](main.py). We then wrap each function in a [`Runnable`](main.py) instance.

We can then chain these functions together using the `|` operator. The result is a new [`Runnable`](main.py) that, when called, will call the first function, pass its result to the second function, and so on.

For example, `(add_five | multiply_by_two | square)(x)` is equivalent to [`square(multiply_by_two(add_five(x)))`](main.py).

## Installation

To use this project, you need to have Python installed on your machine. You can then clone this repository and run [`main.py`](main.py).
