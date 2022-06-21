# function1.py
# 함수를 정의

def times(a,b):
    return a+b, a*b

# 함수를 호출
# 디버깅할 때 중단(중단점)
result = times(3,4)
print(result)

# 불변형식인경우 
a = 1.2
print(id(a))
a = 2.3
print(id(a))
print("가변형식")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

# 참조를 복사 전달
def change(x):
    x[0] = "H"

# 호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출 후 :",wordlist)

# 참조를 복사 전달
def change(x):
    # 복사본(deep copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수내부 : " , x1)

wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출 후 :",wordlist)

# 교집합 함수 (디버깅 연습)
def intersection(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
            
    return result 

# 함수호출
print(intersection("HAM","SPAM"))