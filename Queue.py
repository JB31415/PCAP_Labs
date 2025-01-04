class QueueError(Exception):  # Choose base class for the new exception.
    #
    #  Write code here
    #
    def __init__(self):
        self.message = "Queue is empty"
        super().__init__(self.message)

class Queue:
    def __init__(self):
        #
        # Write code here
        #
        self.__queue = []

    def put(self, elem):
        #
        # Write code here
        #
        self.__queue.insert(len(self.__queue), elem)

    def get(self):
        #
        # Write code here
        #
        if (len(self.__queue) == 0):
            raise QueueError()
            
        temp_val = self.__queue[0]
        del(self.__queue[0])
        return temp_val

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")
