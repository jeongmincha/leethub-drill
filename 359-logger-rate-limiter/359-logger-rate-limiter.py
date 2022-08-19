class Logger:

    def __init__(self):
        self.last_timestamp = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.last_timestamp:
            if timestamp - self.last_timestamp[message] >= 10:
                self.last_timestamp[message] = timestamp
                return True
            else:
                return False
        else:
            self.last_timestamp[message] = timestamp
            return True

# {"foo": 1, "bar": 2}

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)