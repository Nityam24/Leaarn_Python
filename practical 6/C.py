# c) Create a class clock having 3 init parameters – hours, minutes and seconds. Write
# following methods:
# a. setClock – to set the time
# b. displayTime – to show current time
# c. tick – increase the time by one second

class clock:
    def __init__(self,hr,min,sec):
        self.hour=hr
        self.min=min
        self.sec=sec

    def setClock(self,hr,min,sec):
         self.hour=hr
         self.min=min
         self.sec=sec
    
    def displayTime(self):
        print("Hour: ",self.hour)
        print("Minute: ",self.min)
        print("Hour: ",self.sec)

    def tick(self):
        self.sec=self.sec+1
        if self.sec>=60:
            self.sec=self.sec-60
            self.min=self.min+1
            if self.min>=60:
                self.min=self.min-60
                self.hour=self.hour+1
        else:
           pass 

t1 = clock(12,58,59)
t1.displayTime()
t1.setClock(12,59,59)
t1.tick()
t1.displayTime()
