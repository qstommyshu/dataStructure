#stack properties: push, pop, isEmpty, isFull(python stack will never be full), peek, size
class myStack:
    def __init__(self):
        self.items = []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self) :
        return self.items == []
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

stack = myStack()
print(stack.isEmpty())
stack.push(1)
print(stack.peek())
print(stack.size())