__author__ = 'lxy0129'
class stack(object):
    def __init__(self,size=20):
        self.stack = []
        self.size = size;
        self.top = -1

    def setsize(self,size):
        self.size = size



    def push(self,element):
        if self.isfull():
            raise "StackOverFlow"
        else:
            self.stack.append(element)
            self.top += 1

    def pop(self):
        if self.isempty():
            raise "StackUnderflow"
        else:
            element = self.stack[-1]
            #self.size = self.size - 1
            self.top = self.top - 1;
            del self.stack[-1]
            return element

    def empty(self):
         self.stack = []
         self.top = -1;

    def isfull(self):
       if self.top == self.size - 1:
            return True
       else:
            return False

    def isempty(self):
        if self.top == -1:
            return True
        else :
            return False

    def gettop(self):
        return self.top

if __name__ == "__main__":

    stack1 = stack()

    for i in range(10):
        stack1.push(i)
    print stack1.gettop()
    for i in range(10):
       print stack1.pop()
