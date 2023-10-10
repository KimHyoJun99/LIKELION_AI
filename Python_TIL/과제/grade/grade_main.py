import sqlite3
from grade_module import *

con = sqlite3.connect('assignment.db')
cur = con.cursor()

def main(con, cur):
    create_table(cur)
    # dict에 함수 넣어서 사용
    menu_exec = {1: input_grade, 2: output_grade, 3: delete_grade, 4: update_grade, 5: search_grade, 6: sort_grade, 7: save_grade, 8: exit}
    while True:
        menu()
        response = int(input("메뉴를 선택하세요: "))
        if response == 8:
            menu_exec[response](con)
            break
        elif response == 7:
            menu_exec[response](con)
        else:
            if 0< response <7:
                menu_exec[response](cur)
            else:
                print("1 ~ 8 사이의 숫자를 입력해주세요")

if __name__ == '__main__':
    main(con, cur)