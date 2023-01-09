class person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f'hello im {self.name}')

class Coders(person):
    def __init__(self, name,type_speed):
        super().__init__(name)
        self.type_speed = type_speed
    
    def wpm(self):
        print(f'i type {self.type_speed} wpm')

coder1 = Coders('sheraj',106)

coder1.wpm()
coder1.type_speed = 100
coder1.wpm()
