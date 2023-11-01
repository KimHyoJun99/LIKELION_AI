# 함수로 정의한 addressbook 클래스로 변경
# 생성자 사용
# 상속, 오버라이딩 사용

class Book:
    
    def __init__(self):
        self.insert_list = []
    
    def basic_form(self):  # AddressBook class에서 오버라이딩 필요
        print("출력")
        print('=' * 20)
        print("    이름    ISBN")
        print('=' * 20)
        
    def menu(self):  # 오버라이딩 필요 없음
        print("main 메뉴")
        print("1. 입력")
        print("2. 출력")
        print("3. 검색")
        print("4. 종료")
        
    def munu_input(self):  # 오버라이딩 필요
        print("1. 입력")
        name = input("이름: ")
        ISBN = input("ISBN: ")
        self.insert_list.append({"name":name, "ISBN":ISBN})
    
    def menu_output(self):  # 오버라이딩 필요
        self.basic_form()
        print('=' * 20)
        for book in self.insert_list:
            print(f"{book['name']}  {book['ISBN']}")
            
    def menu_search(self):  # 오버라이딩 필요
        print("검색")
        input_value = input("검색할 이름을 입력하세요: ")
        for book in self.insert_list:
            name = book["name"]
            if input_value == name:
                self.basic_form()
                print(f"{book['name']}   {book['ISBN']}")
                break
        else:
            print("찾는 책이 없습니다.")
    
    def menu_exit(self):  # 오버라이딩 필요 없음
        print("종료")
        
    
class AddressBook(Book):
    
    def basic_form(self):
        print("출력")
        print('=' * 20)
        print("  이름  나이    주소")
        print('=' * 20)
        
    def menu_input(self):
        print("1.입력")
        name = input("이름: ")
        age = int(input("나이: "))
        addr = input("주소: ")
        self.insert_list.append(({"name":name, "age":age, "addr":addr}))
        
    def menu_output(self):
        self.basic_form()
        for person in self.insert_list:
            print(f" {person['name']}  {person['age']}    {person['addr']}")
    
    def menu_search(self):
        print("검색")
        input_value = input("검색할 이름을 입력하세요: ")
        for person in self.insert_list:
            name = person["name"]
            if input_value == name:
                self.basic_form()
                print(f" {person['name']}  {person['age']}    {person['addr']}")
                break
        else:
            print("찾는 사람이 없습니다.")
            
    def main(self):
        menu_exec = {1:self.menu_input, 2:self.menu_output, 3:self.menu_search, 4:self.menu_exit}
        
        while True:
            self.menu()
            input_menu = int(input("번호를 입력하세요: "))
            if input_menu == 4:
                self.menu_exit()
                break
            else:
                if 0 < input_menu < 5:
                    menu_exec[input_menu]()
                else:
                    print("1, 2, 3, 4 중에 입력하세요")

if __name__ == '__main__':
    addrbook = AddressBook()
    addrbook.main()