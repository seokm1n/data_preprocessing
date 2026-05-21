scorelist = [["Kor"], ["Eng"], ["Math"]]
print(scorelist)

# 문제
# input() 함수를 이용해서 키보드로 각 과목의 점수를 입력받아 저장
total = 0
for item in range(len(scorelist)):
    scorelist[item].append(int(input(f"{scorelist[item][0]} 과목의 점수를 입력하세요: ")))
    total += scorelist[item][1]
print("="*45)
print(scorelist)  # [["Kor", 90], ["Eng", 80], ["Math", 70]]

# 학생의 총점과 평균을 계산해서 출력
print(f"총점 : {total}")
print("평균 : {0:.2f}".format(total / len(scorelist)))