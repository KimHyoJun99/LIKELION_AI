Person = []

def basic_form():
    print("출력")
    print("="* 20 )               
    print("%10s%10s%10s" %("이름","나이","주소"))
    print("="* 20 )               
    
def menu():
    print("main 메뉴")
    print("1.입력")
    print("2.출력")
    print("3.검색")
    print("4.종료")

def menu_input():
    print("1.입력")
    name = input("이름:")
    age = int(input("나이:"))
    addr = input("주소:")
    Person.append(({"name":name, "age":age, "addr":addr}))

def menu_output():
    basic_form()
    print("="* 20 )
    for dt in Person:
        print("%(name)10s%(age)10d%(addr)10s" %dt)

def menu_search():
    print("검색")
    flag_for_search = False
    input_value  = input("검색할 이름을 입력하세요:")
    for dt in Person:
        temp_name = ("%(name)s" %dt)
        if input_value==temp_name :
            basic_form()
            print("%(name)10s%(age)10d%(addr)10s" %dt)
            flag_for_search = True
            break
    if flag_for_search == False:
        print("찾는사람이 없습니다")
        
def menu_exit():
    print("종료")

