import random

class BaseballGame:
    strike = 0
    count = 0
    
    def start_game(self):
        while True:
            print("1. 게임 시작")
            print("2. 종료")
            response = input("숫자를 입력하세요: ")
            
            if response == '2':
                print("게임이 종료되었습니다.")
                break
            else:
                print("게임이 시작되었습니다.")
                self.answer = random.sample([i for i in range(10)], 3) 
                self.count = 0
                while True:
                    self.compare_answer(self.answer)
                    if self.strike == 3:
                        print(f"결과: {self.count}회 만에 맞추셨습니다.")
                        break
                    
            keep = input("계속하시겠습니까?(y/n) ")
            if keep == 'y':
                continue
            else:
                break
        
    def compare_answer(self, answer):
        self.strike = 0
        ball = 0
        loc = -1
        self.count += 1
        user_answer = input("숫자 3개를 입력하세요: ")
        user_answer = [int(i) for i in user_answer]

        for i in answer:
            loc += 1
            if (i in user_answer) and i == user_answer[loc]:
                self.strike += 1
            elif i in user_answer:
                ball += 1
            else:
                continue
    
        if self.strike == 0 and ball == 0:
            print("Out")
        elif self.strike == 0:
            print(f"{ball} ball")
        elif ball == 0:
            print(f"{self.strike} strike")
        else:
            print(f"{self.strike} strike {ball} ball")
        