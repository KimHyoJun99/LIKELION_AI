import sqlite3

def create_table(cur):
    try:
        q = "CREATE TABLE IF NOT EXISTS grade(name text, kor int, eng int, math int)"
        cur.execute(q)
    except Exception as err:
        print("err : ", err)

def menu():
    print('='*20)
    print("성적 데이터 처리")
    print('='*20)
    print("1. 입력 \n2. 보기 \n3. 삭제 \n4. 수정 \n5. 검색 \n6. 정렬 \n7. 저장 \n8. 종료")

def input_grade(cur):
    print("1) 입력")
    while True:
        name = input("이름: ")
        kor = input("국어: ")
        eng = input("영어: ")
        math = input("수학: ")
        q = "INSERT INTO grade VALUES('"+name+"', '"+kor+"', '"+eng+"', '"+math+"')"
        cur.execute(q)
        continue_ = input("계속 입력하시겠습니까?(y/n): ")
        if continue_ == 'n':
            break
            
def output_grade(cur):
    kor_grade = []
    eng_grade = []
    math_grade = []

    print("2) 보기")
    print('='*30)
    print("   이름   국어   영어   수학   총점   평균   ")
    print('='*30)
    q = "SELECT * FROM grade"
    cur.execute(q)

    while True:
        row = cur.fetchone()
        if row == None:
            break
        name = row[0]
        kor = row[1]
        eng = row[2]
        math = row[3]
        kor_grade.append(int(kor))
        eng_grade.append(int(eng))
        math_grade.append(int(math))
        sum_grade = kor + eng + math
        mean_grade = (kor + eng + math) / 3
        print(f"  {name}   {kor}   {eng}   {math}   {sum_grade}   {mean_grade}   ")
    kor_mean = sum(kor_grade) / len(kor_grade)
    eng_mean = sum(eng_grade) / len(eng_grade)
    math_mean = sum(math_grade) / len(math_grade)
    print('='*30)
    print(f"과목별 평균     {kor_mean}   {eng_mean}   {math_mean}")

def delete_grade(cur):
    print("3) 삭제")
    delete_name = input("삭제할 이름을 입력하세요: ")
    cur.execute("DELETE FROM grade WHERE name = %s", [delete_name])

def update_grade(cur):
    print("4) 수정")
    before_name = input("수정할 이름을 입력하세요: ")
    cur.execute("SELECT * FROM grade WHERE name = %s", [before_name])
    row = cur.fetchone()
    name = row[0]
    kor = row[1]
    eng = row[2]
    math = row[3]
    update_name = input(f"이름 ({name}: )")
    update_kor = int(input(f"국어 ({kor}): "))
    update_eng = int(input(f"영어 ({eng}): "))
    update_math = int(input(f"수학 ({math}): "))
    cur.execute("UPDATE grade SET name = %s, %d, %d, %d WHERE name=%s", [update_name, update_kor, update_eng, update_math, name])

def search_grade(cur):
    print("5) 검색")
    search_name = input("이름을 입력하세요: ")
    cur.execute("SELECT * FROM grade WHERE name=%s", [search_name])
    row = cur.fetchone()
    name = row[0]
    kor = row[1]
    eng = row[2]
    math = row[3]
    sum = kor + eng + math
    mean = (kor + eng + math) / 3
    print('='*30)
    print("   이름   국어   영어   수학   총점   평균   ")
    print('='*30)
    print(f"  {name}   {kor}   {eng}   {math}   {sum}   {mean}   ")

def sort_grade(cur):
    print("6) 정렬")
    q = "SELECT * FROM grade ORDER BY name "
    cur.execute(q)

    kor_grade = []
    eng_grede = []
    math_grade = []
    print('='*30)
    print("   이름   국어   영어   수학   총점   평균   ")
    print('='*30)
    while True:
        row = cur.fetchone()
        if row == None:
            break
        name = row[0]
        kor = row[1]
        eng = row[2]
        math = row[3]
        kor_grade.append(kor)
        eng_grede.append(eng)
        math_grade.append(math)
        sum = kor + eng + math
        mean = (kor + eng + math) / 3
        print(f"  {name}   {kor}   {eng}   {math}   {sum}   {mean}   ")
    kor_mean = sum(kor_grade) / len(kor_grade)
    eng_mean = sum(eng_grede) / len(eng_grede)
    math_mean = sum(math_grade) / len(math_grade)
    print('='*30)
    print(f"과목별 평균     {kor_mean}   {eng_mean}   {math_mean}")

def save_grade(con):
    print("7) 저장")
    save = input("데이터베이스로 저장하시겠습까(y/n)? ")
    if save == 'n':
        pass
    else:
        con.commit()

def exit(con):
    print("8) 종료")
    print("끝")
    con.close()