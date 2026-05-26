# class MyCalList():
#     def __init__(self, arg1, arg2):
#         self.list1 = arg1
#         self.list2 = arg2
#
#     def SumOfList(self):
#         # list_sum = []
#         # # for x, y in zip(self.list1, self.list2):
#         # #     list_sum.append(x + y)
#         # for idx, item in enumerate(self.list1):
#         #     list_sum.append(item + self.list2[idx])
#         # print(list_sum)
#         set1 = set(self.list1)
#         set2 = set(self.list2)
#         print(list(set1 - set2))
#
#
# data = MyCalList([5, 6, 7, 9], [8, 9, 5, 10])
# data.SumOfList()  # [13, 15, 12, 19]
# # [6, 7] or [7, 6]

class StudentScore():
    def __init__(self, *arg):
        self.name = arg[0]
        self.score = arg[1:]

    def TotalScore(self):
        return sum(self.score)

    def ScoreDisplay(self):
        print(self.name, self.TotalScore(), self.TotalScore() / len(self.score))


StudentList = [
    StudentScore("Hong", 80, 60, 70, 90),
    StudentScore("Kim", 90, 70, 80, 85),
    StudentScore("Park", 88, 66, 77, 99),
    StudentScore("Lee", 92, 72, 82, 82)
]

print("이름", "총점", "평균")
for student in StudentList:
    student.ScoreDisplay()

# 이름  총점  평균
# Hong  300  75
# Kim   325  81.25
# Park  330  82.5
# Lee   328  82
