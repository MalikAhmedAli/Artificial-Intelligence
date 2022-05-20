class Queue():
    def __init__(self):
        self.queue = []


    def is_empty(self):
        return not len(self.queue)

    def enqueue(self, element):
        self.queue.append(element)
        return self.queue


    def dequeue(self):
        if self.is_empty():
            return 
        return self.queue.pop(0)

    
    def peek(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.queue[0]
    

if __name__ == '__main__':
    my_queue = Queue()

    my_queue.enqueue("a")
    my_queue.enqueue("b")
    my_queue.enqueue("c")
    print(f"Queue first element: {my_queue.peek()}")
    # Queue first element: a
    
    print(f"The element '{my_queue.dequeue()}' removed from the Queue")
    # The element 'a' removed from the Queue

