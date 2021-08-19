"""
부품찾기 - 계수정렬, 집합 자료형 활용한 풀이
"""

## 계수정렬 이용한 풀이 법

n = int(input())
array = [0] * 10001 

# for i in list(map(int,input().split())):
#     array[i] = 1

for i in input().split():
    array[int(i)] = 1

# 손님이 요청한 부품 총수 
m = int(input())
# 손님이 요청한 부품 번호 
x = list(map(int,input().split()))

for i in x : 
    if array[i] == 1 :
        print('yes', end = " ")
    else:
        print('no', end=" ")



## 집합 자료형을 이용한 풀이법 
# 가게에 있는 부품 총수 (n) , 부품 리스트 (array)
n = int(input())
array = set(map(int,input().split()))

# 손님이 요청한 부품 총수 ( m) , 요청 부품 번호 리스트 (x)
m = int(input())
x = list(map(int,input().split()))

for i in x : 
    # 해당 부품이 존재하는 경우 
    if i in array : 
        print('yes', end =' ')
    else:
        print('no', end =' ')