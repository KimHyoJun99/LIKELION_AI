num1 = 1
num2 = 2

def plus(num1, num2):
    print("This is my plus module", num1 + num2)

class Animal:
    
    def __init__(self, name):
        self.name = name

    def make_sound(self, sound):
        print(f"{self.name}이/가 {sound} 소리를 냅니다")