#문자열(str)

s= ''
str1 ='hello world'
str2 ="hello world"
print(type(s), type(str1), type(str2))
print(isinstance(str2,str))

#여러줄 문자열 정리
str3 = """"ABCDEF
abcdef
가나다라
바사아
자차카다
파하!!!
"""

print(str3)

#여러줄 주석
#여러줄 문자열 사용

"""
주석1
주석2
주석3
"""

#escape
print("hello\nworld\nI say \"Hello World\"")
print('hello\nworld\nI say "Hello World"')

#
#문자열 연산
#
str1 = "First String"
str2 = "Second String"

#1.인덱싱
print(str1[0], str1[2], str1[4])

#2.슬라이싱
str3 = str2[2:5]
print(str3)
print(str2[2:])

#3.연결(+)
print(str1 + " " + str2)
print("First String" " " "Second String")

#에러 : 문자열 객체끼리 +(연결) 연산을 할 수 있다.
name ="홍길동"
age = 40
#print(name + age) 오류 발생! String 처리하기
print(name +str(age))

#반복(*)
print(str1*3)

#len함수
print(len(str2))

# in, not in
print("S" in str2)
print("S" not in str2)

#문자열 객체는 변경할 수 없다(immutable)
#str1[0] ="F"

#서식(formating) - format() 함수
print("name:" + name + "age:" + age + format(age, "d"))
print("name:" + format(name, "s") + "age" + format(age, "d"))

#튜플을 이용한 서식
f = "name:%s", "age:$d"
print(f)
print(f % (name, age))
print("name:%s, age:%d" % (name, age))

#cf C 스타일
#print("name:%s, age:%d" % (name, age))

#서식 - 딕셔너리를 이용한 포매팅
f = "name:%(n)s, age:%(a)d"
print(f % {"n": "둘리", "a": 30})
print(f % {"n": "마이콜", "a": 20})





