class stack:
    def __init__(self,range_list):
        self.range_list=range_list
        self.pointer=0
        self.list_init = [0 for i in range(self.range_list)]
        self.last_operation=None
        self.is__empty=False
        self.counter=0

    def print_init_list(self):
        return self.list_init

    def lenght_array(self):
        return self.counter

    def push(self,value):
        if self.pointer<len(self.list_init):
            self.list_init[self.pointer]=value
            self.pointer+=1
            self.last_operation=1
            self.counter+=1
        else:
            print("Stack Overflow")

    def pop(self):
        if self.is_empty()==True:
            return "Stack Underflow"
        else:
            self.pointer -= 1
            self.counter-=1

    def peak(self):
        return self.list_init[self.pointer-1]

    def is_empty(self):
        if self.pointer==0:
            self.is__empty=True
            return self.is__empty
        else:
            self.is__empty=False
            return self.is__empty



x=stack(5)
print(x.print_init_list())
x.push(10)
x.push(20)
x.push(30)
x.push(40)
print(x.print_init_list())
print(x.peak())
x.pop()
print(x.peak())
x.pop()
print(x.peak())
x.push(69)
print(x.peak())
print(x.print_init_list())
x.pop()
print(x.peak())
x.pop()
print(x.is_empty())
print(x.peak())
x.pop()
print(x.peak())
print(x.pop())
print(x.is_empty())
x.push(69)
x.push(100)
x.push(94)
print(x.lenght_array())