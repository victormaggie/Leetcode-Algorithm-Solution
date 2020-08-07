class Logger:

    def __init__(self):
        self.queue = collections.deque(maxlen=10)
        slelf.set = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        # time complexity o(n)
        while self.queue:
            msg, ts = self.queue[0]

            if timestamp - ts >= 10:
                self.queue.popleft()
                self.set.remove(msg)
            else:
                break
    
        if message not in self.set:
            self.set.add(message)
            self.queue.append((message,timestamp))
            return True
        else:
            return False

# time complexity o(N) the size of queue
# space complexity o(N) the queue or set     
    