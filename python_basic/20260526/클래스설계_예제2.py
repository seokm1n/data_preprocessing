class PersonInfo():
    def __init__(self, name, age, city):
        self.name = name  # 멤버변수화 ==> 멤버변수 등록과 동시 초기화
        self.age = age
        self.city = city

    def Display(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 지역 : {self.city}')


per1 = PersonInfo("Hong", 30, "Seoul")
per2 = PersonInfo("Kim", 50, "Daejeon")
per3 = PersonInfo("Park", 40, "Busan")

PerList = [per1, per2, per3]
print("=" * 50)
for per in PerList:
    per.Display()
    print("=" * 50)
