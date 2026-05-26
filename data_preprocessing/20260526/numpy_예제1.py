import numpy as np

arr2 = np.arange(1, 21).reshape((4, 5))
print(arr2)

# 넘파이 배열 select 문법
print(arr2[1][2])
print(arr2[3][3])

subset = arr2[1:3, 1:3]  # arr2[행슬라이싱, 열슬라이싱]
print(subset)

subset = arr2[:3, :3]  # arr2[행슬라이싱, 열슬라이싱]
print(subset)
