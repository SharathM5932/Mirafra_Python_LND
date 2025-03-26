# class parent:
#     def __init__(self):
#         self.a=1
#         self._b=2
#         self.__c=3
#     def t1(self):
#         return self.a,self._b,self.__c
#
# # o1=parent()
# # print(parent()._b)
#
# class child:
#     aa=parent()._b
#     print(aa)
# print(child())
class outerclass:
    def __init__(self):
        self.outername='outer_instance'

        class innerclass:
            def __init__(self):
                self.innername='inner_instance'

            def display(self):
                return f"inner name is {self.innername}"

    def display(self):
        return f'outer name is {self.outername}'

obj1=outerclass()
obj2=obj1.innerclass()
i=obj1.innerclass()



