import sqlite3

con = sqlite3.connect('assignment.db')
cur = con.cursor()

def create_table(cur):
    try:
        q = "CREATE TABLE IF NOT EXISTS gradeTBL(name text, kor int, eng int, math int)"
        cur.execute(q)
    except Exception as err:
        print("err : ", err)

def input_grade(cur):
    print("1) 입력")
    while True:
        name = input("이름: ")
        kor = input("국어: ")
        eng = input("영어: ")
        math = input("수학: ")
        q = "INSERT INTO gradeTBL VALUES('"+name+"', '"+kor+"', '"+eng+"', '"+math+"')"
        cur.execute(q)
        continue_ = input("계속 입력하시겠습니까?(y/n): ")
        if continue_ == 'n':
            break
            
def output_grade(cur):
    print("2) 보기")
    print('='*30)
    print("   이름   국어   영어   수학   총점   평균   ")
    print('='*30)
    q = "SELECT * FROM gradeTBL"
    cur.execute(q)
    while True:
        row = cur.fetchone()
        name = row[0]
        kor = row[1]
        eng = row[2]
        math = row[3]
        sum = kor + eng + math

def delete_grade(cur):
    pass

def update_grade(cur):
    pass

def search_grade(cur):
    pass

def sort_grade(cur):
    pass

def exit():
    pass