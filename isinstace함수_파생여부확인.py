class Person:
    pass
class Bird:
    pass
# 부모클래스인 Person을 상속받아서 자식클래스인 Student 정의
class Student(Person):
    pass

# 인스턴스를 생성 
p, s = Person(), Student()

print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))