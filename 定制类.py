# -*- coding:utf-8 -*-

class Time60(object):
    MIN_HEX = 60
    HOUR_HEX =24
    def __init__(self ,*val):
           if 1 == len(val) and isinstance(val[0],str):
            try:
             self.hr = int(val[0].split(':')[0])
             self.mn = int(val[0].split(':')[1])
            except (TypeError,IndexError):
                    print 'Invalid parameter.'
           elif 2 == len(val):
               self.hr = val[0]
               self.mn = val[1]
           else:
                 print '__init__() takes exactly two argument.'
    def __str__(self):
             return '%02d:%02d' %(self.hr,self.mn)
    __repr__ = __str__
    def __add__(self,other):
           tup = self.hexe(self.hr + other.hr,self.mn
                                      + other.mn)
           return self.__class__(tup[0],tup[1])
    def __iadd__(self,other):
            self.hr += other.hr
            self.mn += other.mn
            self.hr,self.mn = self.hexe(self.hr,self.mn)
            return self
    def hexe(self,hours,mins):
             if mins >= self.MIN_HEX:
                      mins -= self.HOUR_HEX
                      hours += 1
             if hours >= self.HOUR_HEX:
                    hours -= self.HOUR_HEX
             return (hours,mins)

mon = Time60(11,35)
tue = Time60(10,45)
print mon + tue


