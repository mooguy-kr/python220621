# db1.py

import sqlite3

# 연결객체를 리턴받기 (메모리에 생성-연습)
con = sqlite3.connect(":memory:")
# 커서객체를 리턴받기
cur = con.cursor()
# 테이블(스키마)를 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
# 1건 입력(insert)
cur.execute("insert into PhoneBook values('derick','010-222');")
# 입력 파라미터 처리 
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values(?,?);",(name,phoneNumber))
# 여러건을 입력
datalist = (("tom","010-345"),("dsp","010-456"))
cur.executemany("insert into PhoneBook values(?,?);",datalist)

# 검색
cur.execute("select * from PhoneBook;")

# 검색메서드 사용 (패치할때마다 버퍼에서 삭제됨)
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
print(cur.fetchall())

# for row in cur:
#     # row 는 tuple로 받아짐 
#     print(row)
#     # print(row[0])
#     # print(row[1])

