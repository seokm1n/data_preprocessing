import numpy as np
import pandas as pd

# 사전을 활용해서 DataFrame 객체 생성
dictdata = {"Hong": [90, 80, 70, 60, 75], "Kim": [85, 95, 65, 55, 75], "Park": [88, 93, 75, 72, 75],
            "Lee": [55, 66, 77, 92, 75]}
# 위 사전을 활용해서 DataFrame 객체 생성
scoredf = pd.DataFrame(dictdata, index=["Kor", "Eng", "Math", "Music", "Sci"])
print(scoredf)
# Kim의 점수가 70점 이상인 행만 추출
print(scoredf["Kim"] >= 70)  # Boolean 배열 출력
# 불린 배열을 색인 인덱스로 사용해서 추출 ==> 불린 색인 ==> loc만 지원
# 불린 배열의 True 항목만 자동 추출, Kim과 Park만
subset = scoredf.loc[scoredf["Kim"] >= 70, ["Hong", "Park"]].copy()
print(subset)
print("=" * 80)

print(scoredf)
# 특정 컬럼 데이터 선택
print(scoredf[["Hong", "Park"]])  # 여러 컬럼 각각 선택 ==> 리스트
