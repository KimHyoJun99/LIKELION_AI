import random

class BaseballGame:
    def selectNumbers(self):
        samples = [n for n in range(1, 10)]
        random.shuffle(samples)
        self._data = samples[0:3]
       

    def verifyinput(self, value):
        if value < 1 or value > 9:
            raise Exception("Wrong number entered. Please, try again")
        
    def getNumbers(self):
        print("Enter 3 numbers (1 ~ 9)(input exam:3 6 9):", end="")
        try:
            s1 = input("")
            n1 = int( s1[0] )
            n2 = int( s1[2] )
            n3 = int( s1[4] )
            self.verifyinput(n1)
            self.verifyinput(n2)
            self.verifyinput(n3)
        except Exception as ex:
            print("error",ex)
            return list()
        else:
            return [n1, n2, n3]

    def judge(self, numbers):
        strikes = 0
        balls = 0
        for i in range(3):
            if self._data[i] == numbers[i]:
                strikes += 1
            elif numbers[i] in self._data:
                balls += 1
        return strikes, balls

    def playball(self):
        self.selectNumbers()
        is3Strikes = False
        count = 0
        while is3Strikes == False:
            numbers = self.getNumbers()
            if len(numbers) < 3:
                continue
            judgeResult = self.judge(numbers)
            is3Strikes = (judgeResult[0] == 3)
            if is3Strikes == False:
                print("Result: %d stike(s) and %d ball(s)" % judgeResult)
            count += 1
        print("You got the game in %d times" % count)

    def startGame(self):
        while True:
            print("Baseball Game")
            print("-" * 30)
            print("1. Playball~")
            print("2. Quit game")
            
            menu = int(input("select Num:"))
            if menu == 2:
                break
            self.playball()

if __name__ == '__main__':
    game = BaseballGame()
    game.startGame()
    
