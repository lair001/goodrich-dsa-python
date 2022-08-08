from solutions.vendor.ch06.array_stack import ArrayStack as Ch6ArrayStack


def transfer(S: Ch6ArrayStack, T: Ch6ArrayStack):
    while not S.is_empty():
        T.push(S.pop())
