"""
[이진 탐색 소스 코드 - 재귀 구현]
    # 입력예시1 
        10 7
        1 3 5 7 9 11 13 15 17 19    
    # 출력예시1
        4

    # 입력예시2 
        10 7
        1 3 5 6 9 11 13 15 17 19    
    # 출력예시2
        원소가 존재하지 않습니다. 
"""

def binary_search(array, target, start, end):
    if start > end : 
        return None

    mid = ( start + end )//2
    print(f"mind >> {mid}")
    #찾은 경우 중간점 인덱스 반환 
    if array[mid] == target: 
        return mid 
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인 
    elif array[mid] > target : 
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)


# n (원소의 개수)과 target(찾고자 하는 값)을 입력 받기 
n, target = list(map(int, input().split()))       # 입력이 3개가 되는 순간 ValueError: too many values to unpack 출력됨
# 전체 원소 입력 받기 
array = list(map(int,input().split()))


# 이진 탐색 수행 결과 출력 
result = binary_search(array, target, 0, n-1)
if result == None : 
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
