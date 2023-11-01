# 과제: 주소록을 입력받아 결과를 출력

import pymysql

def delete_addressbook():
    con = pymysql.connect(host="127.0.0.1", user="root", password="#####", db="shopDB", charset="utf8")
    cur = con.cursor()
    cur.execute("DROP TABLE addressBook")

def address_book():
    con = pymysql.connect(host="127.0.0.1", user="root", password="#####", db="shopDB", charset="utf8")
    cur = con.cursor()
    cur.execute("CREATE TABLE addressBook (userName char(10), age int, userAddress char(15))")

    while True:
        print("메인 메뉴)")
        print("\t1. 입력 \n\t2. 출력 \n\t3. 검색 \n\t4. 종료 \n")
        num = int(input("번호를 입력하세요: "))

        if num == 4:
            break
        else:
            if num == 1:
                while True:
                    data1 = input("이름: ")
                    data2 = input("나이: ")
                    data3 = input("주소: ")
                    cur.execute("INSERT INTO addressBook VALUES('"+data1+"', "+data2+", '"+data3+"')")
                    continue_ = input("계속 입력하시겠습니까 (y/n)? ")

                    if continue_ == 'n':
                        con.commit()
                        break
            elif num == 2:
                cur.execute("SELECT * FROM addressBook")
                print('-' * 30)
                print("   이름   나이       주소")
                print('-' * 30)
                while True:
                    row = cur.fetchone()
                    if row == None:
                        break
                    data1 = row[0]
                    data2 = row[1]
                    data3 = row[2]
                    print(f"  {data1}   {data2}    {data3}")
                print()
            else:
                name = input("검색할 이름을 입력하세요: ")
                print('-' * 30)
                print("   이름   나이       주소")
                print('-' * 30)
                cur.execute("SELECT * FROM addressBook WHERE userName = %s", [name])
                row = cur.fetchone()
                if row == None:
                    break
                data1 = row[0]
                data2 = row[1]
                data3 = row[2]
                print(f"  {data1}   {data2}    {data3}")
                print()
    con.close()