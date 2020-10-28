class Queue(object):
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return self.queue == []
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    def peek(self):
        return self.queue[0]
s1 = Queue()
s1.enqueue(10)
s1.enqueue(32)
s1.enqueue(45)
print("Dequeue:",s1.dequeue())
print("peek :",s1.peek())
print(len(s1.queue))

        
