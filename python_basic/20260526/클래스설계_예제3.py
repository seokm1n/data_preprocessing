class MyCalData():
    def __init__(self, *args):
        self.person = args

    def AvgDisplay(self):
        total = 0
        for item in self.person:
            total += item[1]
        print(f"평균 : {total / len(self.person)}")

data = MyCalData(["Kim", 100], ["Park", 90], ["Hong", 70])
data.AvgDisplay()  # (100 + 90 + 70) / 3 평균 출력
