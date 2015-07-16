class time60(object):
    def __init__(self,hour,min):
        self.hour = hour
        self.minute = min
    def __str__(self):    #主要用于定制输出格式
        return '%d:%d' %(self.hour,self.minute)

mon = time60(10,30)
print mon
