
class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)



stack = Stack()
stack.push(8)
stack.push(15)
stack.push(18)
print(stack)
print(stack.pop())
print(stack.peek())
stack.push(33)
print(stack)
