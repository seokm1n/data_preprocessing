class MyComInfo():
    def __init__(self, arg1="Python Academy"):  # 디폴트 파라미터
        self.name = arg1

    def DisplayName(self):
        print(self.name)

    def SettingName(self, arg2):
        self.name = arg2  # 멤버변수에 arg을 대입해서 멥버변수 내용 수정


com1 = MyComInfo("AI Academy")
com1.DisplayName()  # AI Academy 출력

com2 = MyComInfo()
com2.DisplayName()  # Python Academy 출력

com2.SettingName("Agent Academy")
com2.DisplayName()  # Agent Academy 출력
