"""
[정렬된 배열에서 특정 수의 개수 구하기]

(문제설명)
    - N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 
      이때 이 '수열에서 x가 등장하는 횟수를 계산'하세요. 
      예를 들어 수열 {1,1,2,2,2,2,3} 이 있을때 x = 2 라면 현재 수열에서 값이 2인 
      원소가 4개이므로 4를 출력합니다.
    - 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 
      시간 초과 판정을 받습니다.

(입력조건)
    - 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다. 
      ( 1 <= N <= 1,000,000 ), ( -10^9 <= x <= 10^9 )
    - 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다.
      ( -10^9 <= 각 원소의 값 <= 10^9 )

(출력조건)
    - 수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다. 
      단, 값이 x인 원소가 하나도 없다면 -1을 출력합니다. 

# 입력예시
    7 2 
    1 1 2 2 2 2 3

# 출력예시
    4
----------------
- 시간복잡도 O(logN)으로 동작하는 알고리즘을 요구하고 있습니다. 
  > 일반적인 '선형 탐색(Linear Search)로는 시간 초과 판정'을 받습니다.
  > 하지만 데이터가 정렬되어 있기 때문에 '이진 탐색을 수행'할 수 있습니다. 
- 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 파이를 계산해 문제 해결 가능 

"""
# 강의 초반에 언급해서 기억하고 작성함 
from bisect import bisect_left,bisect_right

def discet_func(arr, left_value, right_value):
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)
    return right_index - left_index

n,x = map(int, input().split())
array = list(map(int,input().split()))

# 값이 [x,x] 범위에 있는 데이터의 개수 계산 
count = discet_func(array, x, x)

# 값이 x인 원소가 존재하지 않는다면 
if count == 0 : 
    print(-1)
else:
    print(count)