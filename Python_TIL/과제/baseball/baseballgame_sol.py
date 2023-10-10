import random

class BaseballGame:
    def selectNumbers(self):
        samples = [n for n in range(1, 10)]  # 리스트 컴프리헨션
        random.shuffle(samples)  # 랜덤으로 섞은 후
        self._data = samples[0:3]  # 리스트의 0~2번째 위치까지 반환
        
        # self.data = random.sample([i for i in range(10)], 3)
       
    # 예외처리 메서드
    def verifyinput(self, value):
        if value < 1 or value > 9:
            raise Exception("Wrong number entered. Please, try again")
        
    def getNumbers(self):
        print("Enter 3 numbers (1 ~ 9)(input exam:3 6 9):", end="")
        try:
            s1 = input("")  # s1 = list(map(int, input().split()))
            n1 = int( s1[0] )  # 띄어쓰기가 포함되어 있어서 짝수 index만 가져오기
            n2 = int( s1[2] )
            n3 = int( s1[4] )
            self.verifyinput(n1)  # 예외 처리 메서드
            self.verifyinput(n2)
            self.verifyinput(n3)
        except Exception as ex:
            print("error",ex)
            return list()  # except에 걸리면 빈 리스트 반환
        else:
            return [n1, n2, n3]  # 입력 리스트 반환

    def judge(self, numbers):
        strikes = 0
        balls = 0
        for i in range(3):
            if self._data[i] == numbers[i]:  # 위치와 숫자가 같으면 strikes 증가
                strikes += 1
            elif numbers[i] in self._data:  # 포함만 되어 있으면 balls 증가
                balls += 1
        return strikes, balls

    def playball(self):
        self.selectNumbers()  # selectNumbers 메서드
        is3Strikes = False
        count = 0
        while is3Strikes == False:
            numbers = self.getNumbers()  # getNumbers 메서드
            if len(numbers) < 3:
                continue  #  입력 받은 숫자가 3보다 적으면 반복문 처음으로
            judgeResult = self.judge(numbers)  # judge 메서드
            is3Strikes = (judgeResult[0] == 3)  # return 받은 strike가 3이면 True
            if is3Strikes == False:
                print("Result: %d stike(s) and %d ball(s)" % judgeResult)
            count += 1  # 시행 횟수 증가
        print("You got the game in %d times" % count)  # 반복문이 종료되면 출력

    def startGame(self):
        while True:
            print("Baseball Game")
            print("-" * 30)
            print("1. Playball~")
            print("2. Quit game")
            
            menu = int(input("select Num:"))
            if menu == 2:
                break
            self.playball()  # playball 메서드

if __name__ == '__main__':
    game = BaseballGame()  # BaseballGame class
    game.startGame()  # startGame 메서드 실행
    
