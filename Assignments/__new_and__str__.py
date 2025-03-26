#__str__
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def add(self):
        return f"{self.age} is your age"

    def __str__(self):
        return f"MyClass(name={self.name}, age={self.age})"

obj = MyClass("Alice", 30)
print(obj)


#__new__
class myclass:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance")
        instance = super().__new__(cls)  # Call the base class `__new__`
        return instance
    def __init__(self,a):
        print("initializing instance")
        self.a=a

a1=myclass(3)


