#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# class로 주소록 만들기


# In[ ]:


class Addr:  # 부모 클래스 생성
    
    def __init__(self):  # 생성자로 변수생성 및 초기화
        self.Person = []
        self.input_num = 0
        self.name = ""
        self.age = 0
        self.addr = ""   
        
    def basic_form(self):  # 출력, 조회를 위한 기본 포맷
        print("=" * 40)
        print("%10s%10s%10s" %("이름","나이","주소"))
        print("=" * 40)
    
    def menu_input(self):  # 입력 서비스 구현 매소드
        print("입력을 선택하셨습니다! ")
        self.name = input("이름: ")
        self.age = int(input("나이: "))
        self.addr = input("주소: ")
        self.Person.append(({"name":self.name, "age":self.age, "addr":self.addr}))
    
    def menu_output(self):  # 출력 서비스 구현 매소드
        print("출력을 선택하셨습니다!")
        self.basic_form()
        
        for dt in self.Person:  # 리스트에 들어있는 값을 출력하는 반복문
            print("%(name)10s%(age)10d%(addr)10s" %dt)
            
    def menu_search(self):  # 검색 서비스 구현 매소드
        print("검색을 선택하셨습니다.")
        flag_for_search = False
        input_value = input("검색할 이름을 입력해주세요: ")
        for dt in self.Person:
            temp_name = ("%(name)s" %dt)
            if input_value == temp_name:
                self.basic_form()
                print("%(name)10s%(age)10d%(addr)10s" %dt)
                flag_for_search = True
                break
        if flag_for_search == False:
            print("찾는 사람이 주소록에 없습니다.")
                
    
    def start(self):  # 시작하는 매소드
        while True:
            print("주소록 서비스입니다. :) ")
            print("=" * 40)
            print("1. 입력")
            print("2. 출력")
            print("3. 검색")
            print("4. 종료")
            print("=" * 40)

            input_num = int(input("원하시는 서비스 번호를 입력해주세요: "))
            if input_num == 4:
                print("서비스를 종료합니다. 감사합니다.")
                break
            else:
                if input_num == 1:
                    self.menu_input()
                elif input_num == 2:
                    self.menu_output()
                elif input_num == 3:
                    self.menu_search()
                else:
                    print("1부터 4까지의 서비스 번호 중 원하시는 번호를 입력해주세요.")  
                    
# 자식 클래스 생성
class StudentAddr(Addr):  #Addr 부모 클래스를 상속받는 자녀 클래스
    def __init__(self):  # 기존 상속과 더불어 school 변수를 생성 및 초기화하는 생성자 
        self.school = ""
        self.Person = []
        self.input_num = 0
        self.name = ""
        self.age = 0
        self.addr = ""   
        
    def start(self, school):  # school을 변수로 받는 매소드
        self.school = school
        while True:
            print(f"{self.school} 학교 학생의 주소록 서비스입니다. :) ")
            print("=" * 40)
            print("1. 입력")
            print("2. 출력")
            print("3. 검색")
            print("4. 종료")
            print("=" * 40)

            input_num = int(input("원하시는 서비스 번호를 입력해주세요: "))
            if input_num == 4:
                print("서비스를 종료합니다. 감사합니다.")
                break
            else:
                if input_num == 1:
                    self.menu_input()
                elif input_num == 2:
                    self.menu_output()
                elif input_num == 3:
                    self.menu_search()
                else:
                    print("1부터 4까지의 서비스 번호 중 원하시는 번호를 입력해주세요.")  


# In[ ]:


# 코드 실행

if __name__ == '__main__':
    addr1 = StudentAddr()  # 자녀 클래스를 인스턴스화
    addr1.start('Techit')


# In[ ]:




