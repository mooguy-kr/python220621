# DemoFile.py

url = "http://www.credu.com/?page=" + str(1)
print(url)

print("서식을 지정")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("0으로 채우기")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(3))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))  
print("{0:.2f}".format(4/3))

# 파일을 생성하기 
f = open("c:\\work\\demo.txt","wt")
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 파일을 읽기 
f = open("c:\\work\\demo.txt","rt")
result = f.read()
print(result)
f.close()

# 기존 파일에 첨부하는 경우 (Append, Read+Write)
f = open("c:\\work\\demo.txt","a+")
f.write("새로운데이터\n")
f.close()

# 한줄씩 읽어오기
f = open("c:\\work\\demo.txt","rt")
# print함수 처리시 줄바꿈 삭제 (end="")
print(f.readline(), end="")
print(f.readline(), end="")

print(f.tell())
f.seek(0)
lst = f.readlines()
print(lst)

f.close()

for item in lst:
    # 출력시 개행문자(\n)를 공백으로 치환(replace)
    print(item.replace("\n",""))