#41강
while True:
    string_input = input("정수 입력> ")
    if string_input.isdigit():
        number_input_a = int(string_input)
        print("원의 반지름:", number_input_a)
        print("원의 둘레:", 2 * 3.14 * number_input_a)
        print("원의 넓이:", 3.14 * number_input_a * number_input_a)
        break
    else:
        print("정수를 입력해주세요!")
#42강
numbers = [52, 273, 32, 103, 90, 10, 275]
print("# (2) 요소 내부에 없는 값 찾기")
number = int(input('숫자 입력 힌트 52'))
try:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
except:
    print("-리스트 내부에 없는 값입니다.")
#43강
def test():
    print("test() 함수의 척 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        sdf.sdf()
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
        return
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() over")
test()
#45강
class 학생:
    def __init__(self, n, k, m, e, s):
        self.n = n
        self.k = k
        self.m = m
        self.e = e
        self.s = s
    def 총점(self):
        return self.k + self.m + self.e + self.s
    def 평균(self):
        return self.총점() / 4
    def 출력(self):
        print(self.n, self.총점(), self.평균(), "\t")
students = [
    학생('a', 97, 98, 88, 95),
    학생('b', 92, 98, 96, 98),
    학생('c', 76, 96, 94, 90),
    학생('d', 98, 93, 96, 92),
    학생('e', 95, 98, 98, 98),
    학생('f', 94, 88, 92, 92)
    ]
print("이름", "총점", "평균", "\t")
for student in students:
    student.출력()
class Studentss:
    def __init__(self, 이름, 나이):
        print("객체 생성")
        self.이름 = 이름
        self.나이 = 나이
    def __del__(self):
        print("객체 소멸")
    def 출력(self):
        print(self.이름, self.나이)
Studentss = Studentss("윤인성", 3)
Studentss.출력()