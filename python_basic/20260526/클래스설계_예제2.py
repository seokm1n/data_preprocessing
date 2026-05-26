class PersonInfo():
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def Display(self):
        print("이름 : ", self.name, ", ", end='')
        print("나이 : ", self.age, ", ", end='')
        print("지역 : ", self.city)


per1 = PersonInfo("Hong", 30, "Seoul")
per2 = PersonInfo("Kim", 50, "Daejeon")
per3 = PersonInfo("Park", 40, "Busan")

PerList = [per1, per2, per3]
print("=" * 50)
for per in PerList:
    per.Display()
    print("=" * 50)
