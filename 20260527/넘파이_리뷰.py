import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr1 = np.array([[3, 4, 5], [6, 7, 8]])  # 넘파이 배열 생성(2행3열)
print(arr1)
print(arr1.ndim)  # 차원수
print(arr1.shape)  # 형태를 튜플로 반환
# axis=0 ==> 행축
# axis=1 ==> 열축

arr2 = np.arange(10, 20).reshape((2, 5))  # 넘파이 범위 데이터 배열
print(arr2)
print("=" * 80)

arr3 = np.random.randint(1, 100, (5, 2))  # 임의의 난수 배열
print(arr3)
print("=" * 80)

arr4 = np.array([[3, 4, 5], [13, 14, 15], [23, 24, 25], [33, 34, 35]])
print(arr4, arr4.shape)
print("=" * 80)

# .copy() ==> 뷰 관계를 끊고 완벽한 사본 객체 생성
subset = arr4[1:3, 1:].copy()
print(subset)
print("=" * 80)

# subset 배열의 15를 100으로 수정하고
# subset 배열과 원본 arr4 배열 출력
subset[0, 1] = 100
print(subset)
print(arr4)
