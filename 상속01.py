#  부모 클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

    def methodA(self):
        print("부모쪽 코드 실행")

# 자식 클래스 정의
class Student(Person):
    # 상속받은 메서드를 덮어쓰기 (재정의,override)
    def __init__(self, name, phoneNumber, subject, studentID):
        # 명시적으로 부모의 생성자 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    def printInfo(self):
        print("Info(name:{0}, Phone Number:{1})".format(self.name,self.phoneNumber))
        print("Info(subject:{0}, studentID:{1})".format(self.subject,self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")

# __dict__ : object클래스에 정의된 스페별멤버변수
# print(p.__dict__)
# print(s.__dict__)

p.printInfo()
s.printInfo()
p.methodA()
s.methodA()

