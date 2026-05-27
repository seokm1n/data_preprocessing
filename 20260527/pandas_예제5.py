import numpy as np
import pandas as pd

# 사전을 활용해서 DataFrame 객체 생성
dictdata = {"Hong": [90, 80, 70, 60, 75], "Kim": [85, 95, 65, 55, 75], "Park": [88, 93, 75, 72, 75],
            "Lee": [55, 66, 77, 92, 75]}
# 위 사전을 활용해서 DataFrame 객체 생성
scoredf = pd.DataFrame(dictdata, index=["Kor", "Eng", "Math", "Music", "Sci"])
print(scoredf)

# 삭제 문법
# 특정 컬럼 하나 삭제할 때 유용 ==> del 키워드
# del scoredf["Park"]
# print(scoredf)

# 특정 컬럼(행)이나 여러개의 컬럼 삭제 메서드 ==> drop
# default 사본 객체 생성, inplace=True ==> 원본 직접 반영, 리턴값 없음
# print("=" * 80)
# print(scoredf.drop(["Hong", "Park"], axis=1, inplace=True))
# print("=" * 80)
# print(scoredf)

# 영어, 음악 삭제
print("=" * 80)
print(scoredf.drop(["Eng", "Music"]))
