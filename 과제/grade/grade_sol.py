# -*- coding:ms949 -*-
import sqlite3

def printMenu():
    print("="*22)
    print("성적데이터 처리")
    print("="*22)
    print("1. 입력", "2. 보기", "3. 삭제", "4. 수정", "5. 검색", "6. 정렬", "7. 저장", "8. 종료", sep='\n')
    return input("메뉴를 선택하세요 : ")

def doInput(cur):
    cont = 'y'
    while(cont == 'y'):
        name    = input("이름 : ")
        korean  = input("국어 : ")
        english = input("영어 : ")
        math    = input("수학 : ")
        q = "insert into scores(name, korean, english, math) values(?, ?, ?, ?)"
        cur.execute(q, (name, korean, english, math))
        cont = input("계속 입력하시겠습니까(y/n)?")

def doShow(cur):
    print("=" * 36)
    print("%10s%10s%10s%10s%10s%10s"%('이름','국어','영어','수학','총점','평균'))
    print("=" * 36)
    q = "select * from scores"
    cur.execute(q)
    ks = 0
    es = 0
    ms = 0
    c = 0
    for n, k, e, m in cur:
        print("%10s%9d%6d%6d%7d%5d"%(n,k,e,m,(k+e+m),(k+e+m)/3))
        ks += k
        es += e
        ms += m
        c += 1
    print("=" * 36)
    if c != 0:
        print("%7s%8d%6d%6d"%("과목별 평균",ks/c, es/c, ms/c))

def doDelete(cur):
    name = input("삭제할 이름을 입력하세요 : ")
    q = "delete from scores where name=?"
    cur.execute(q, (name,))

def doUpdate(cur):
    name = input("수정할 이름을 입력하세요 : ")
    q = "select * from scores where name=?"
    cur.execute(q, (name,))
    lst = cur.fetchall()
    if len(lst) != 0 :
        uname   = input("이름 (%s): "%(lst[0][0]))
        korean  = input("국어 (%d): "%(lst[0][1]))
        english = input("영어 (%d): "%(lst[0][2]))
        math    = input("수학 (%d): "%(lst[0][3]))
        q = "update scores set name=?, korean=?, english=?, math=? where name=?"
        cur.execute(q, (uname, korean, english, math, name))
    
def doSearch(cur):
    name = input("이름을 입력하세요 : ")
    q = "select * from scores where name=?"
    cur.execute(q, (name,))
    print("=" * 36)
    print("%10s%10s%10s%10s%10s%10s"%('이름','국어','영어','수학','총점','평균'))
    print("=" * 36)
    for n, k, e, m in cur:
        print("%10s%9d%6d%6d%7d%5d"%(n,k,e,m,(k+e+m),(k+e+m)/3))

def doSort(cur):
    print("=" * 36)
    print("%10s%10s%10s%10s%10s%10s"%('이름','국어','영어','수학','총점','평균'))
    print("=" * 36)
    q = "select * from scores order by name"
    cur.execute(q)
    ks = 0
    es = 0
    ms = 0
    c = 0
    for n, k, e, m in cur:
        print("%10s%9d%6d%6d%7d%5d"%(n,k,e,m,(k+e+m),(k+e+m)/3))
        ks += k
        es += e
        ms += m
        c += 1
    print("=" * 36)
    if c != 0:
        print("%7s%8d%6d%6d"%("과목별 평균",ks/c, es/c, ms/c))


def doCommit(cur):
    yn = input("데이터베이스로 저장하시겠습니까(y/n)?")

def createTable(cur):
    try :
        q = "create table if not exists scores(name text, korean int, english int, math int)"
        cur.execute(q)
    except Exception as err:
        print("err:", err)

def main():
    dictMenu = {'1':doInput, '2':doShow, '3':doDelete, '4':doUpdate, '5':doSearch, '6':doSort, '7':doCommit}

    try :
        db = sqlite3.connect('homework.db') # Create a database file if it is not available or just connect.
        cur = db.cursor()
        createTable(cur)
        while(1):
            menu = printMenu()
            func = dictMenu.get(menu, '8')
            if func == '8' : break;
            func(cur)
        db.commit()
        db.close()
    except Exception as err:
        print("err:", err)
    
    print("끝")    

if __name__ == '__main__':
    main()
