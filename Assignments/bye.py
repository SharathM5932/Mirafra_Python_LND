print("Welcome to Python Program")
def sub(a,b):
    return a-b
class Hello:
    def __init__(self,lname,fname):
        self.lname=lname
        self.fname=fname
    def concat(self):
        print("Hi this is method1")
        print(self.fname+" "+self.lname)
class B(Hello):
    def __init__(self,lname,fname):
        super().__init__(lname,fname)
    def lower(self):
        print(self.lname.lower()+" "+self.fname)
