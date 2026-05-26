class MyDataControl():
    def __init__(self, *args):  # 튜플 형태로 매개변수 반환
        self.data = (args)
        print("객체 생성 완료!!")
        # 멤버변수 등록하고 초기화

    def SumOfData(self):
        total = 0
        for i in self.data:
            total += i
        print('total : ', total)  # 합을 출력


# 객체생성 ==> 객체가 생성될 때 "객체 생성 완료!!" 를 출력
value = MyDataControl(50, 60, 70, 80, 90)  # 객체를 메모리에 생성했으면 변수로 참조해야함
value.SumOfData()  # 합을 출력
