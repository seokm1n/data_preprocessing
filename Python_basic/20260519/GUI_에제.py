# 기본 제공 GUI 라이브러리 ==> tkinter
import tkinter as tk


def IncreaseFuc():
    numcnt.set(numcnt.get() + 1)


def DecreaseFuc():
    numcnt.set(numcnt.get() - 1)


mywind = tk.Tk()  # main 윈도우 객체 생성
mywind.title("나만의 윈도우")
mywind.geometry("600x600+500+200")  # 윈도우 사이즈 조절 및 출력 위치 조절

numcnt = tk.IntVar()  # 제어변수 : 내부 프로그램 메모리 값과 GUI 표시 데이터의 연동 변수 역할
numcnt.set(0)  # 제어변수에 값 설정

lb1 = tk.Label(text="numbering", textvariable=numcnt, padx=50, pady=50, font=20)
lb1.pack()

# 버튼 자식 윈도우 생성
b1 = tk.Button(text='Increase', padx=50, pady=50, font=20, background="#9FFCFD",
               command=IncreaseFuc, repeatdelay=25, repeatinterval=25)
# 자식 윈도우를 부모 윈도우에 배치 (grid, pack, place)
b1.pack(padx=10, pady=10)

b2 = tk.Button(text='Decrease', padx=50, pady=50, font=20, background="pink",
               command=DecreaseFuc, repeatdelay=25, repeatinterval=25)
b2.pack(padx=10, pady=10)

mywind.mainloop()  # 윈도우 객체를 화면에 계속 갱신해서 출력
