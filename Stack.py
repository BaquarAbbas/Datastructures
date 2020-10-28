class stack(object):
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return self.stack == []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    def peek(self):
        return self.stack[-1]
s1 = stack()
s1.push(10)
s1.push(32)
s1.push(45)
print("popped item is :",s1.pop())
print("peek :",s1.peek())

        
