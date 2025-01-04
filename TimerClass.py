def format_time(hours, minutes, seconds):
    return (str(hours) + ":" + str(minutes) + ":" + str(seconds))

class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        #
        # Write code here
        #
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return (format_time(self.hours, self.minutes, self.seconds))

    def next_second(self):
        #iterate Seconds
        self.seconds += 1
        
        #If seconds above 60, set seconds to zero and minutes to +1
        if(self.seconds > 59):
            self.seconds = 0
            self.minutes += 1
        
        
        if(self.minutes > 59):
            self.minutes = 0
            self.hours += 1
        
        if(self.hours > 23):
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

    def prev_second(self):
        #iterate Seconds
        self.seconds += -1
        
        #If seconds above 60, set seconds to zero and minutes to +1
        if(self.seconds < 0):
            self.seconds = 59
            self.minutes += -1
        
        
        if(self.minutes < 0):
            self.minutes = 59
            self.hours += -1
        
        if(self.hours < 0 ):
            self.hours = 23
            self.minutes = 59
            self.seconds = 59


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
