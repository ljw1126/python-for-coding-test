"""
[부품찾기(p197)] -- 이진탐색, 집합자료형 set(), 계수 정렬 풀이방법이 있음 

(문제 설명)
- 동빈이네 전자 매장에는 부품이 N개가 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 
  어느 날 손님이 M개의 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
  동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 
  이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.

(입력조건)
- 첫째 줄에 정수 N이 주어진다. ( 1 <= N <= 1,000,000 )
- 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 
  이때 정수는 1보다 크고 1,000,000 이하 이다.
- 셋째 줄에는 정수M이 주어진다. ( 1 <= M <= 1,000,000 )
- 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.
  이때 정수는 1보다 크고 1,000,000 이하 이다.

(출력조건)
- 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를 없으면 no를 출력한다. 

# 입력예시

5            # 가게 부품 총수 
8 3 7 9 2    # 가게 부품번호 
3            # 손님이 요청한 부품 총수 
5 7 9        # 손님이 요청한 부품 번호 
"""
## 내가 작성한 코드 ( 정상 동작 )
# def binary_search(array, target, start, end):
#     if start > end : return -1 
#     mid = (start + end )//2 

#     if array[mid] == target : 
#         return mid 

#     elif array[mid] < target :
#         return binary_search(array, target, mid+1 , end)
#     else :     
#         return binary_search(array, target, start , mid - 1)


# # 가게 부품 총 수와 부품종류 
# n = int(input())
# n_array = list(map(int,input().split()))
# n_array.sort()

# # 손님 요청한 부품 총수와 부품번호 
# m = int(input())
# m_array = list(map(int,input().split()))
# m_array.sort()

# for i in m_array:
#     if binary_search(n_array,i,0, n) != -1:
#         print("yes",end=" ")
#     else:
#         print("no", end=" ")


## 해설 답안 ( 반복문 사용 )


def binary_search(array, target, start, end):

    while(start <= end):
        mid = (start + end )//2 

        if array[mid] == target : return mid 
        # 요부분 참 헷갈리네 
        elif array[mid] > target:
            end = mid - 1
        else : 
            start = mid + 1
    return None


# 가게 부품개수 n 입력 
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력 
array = list(map(int,input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전 정렬 

# 손님이 확인 요청한 부품개수 m 입력 
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백 구분하여 입력 
x = list(map(int,input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인 
for i in x : 
    # 해당 부품이 존재하는 지 확인 
    result = binary_search(array, i , 0 , n-1)
    if result != None:
        print("yes" , end = " ")
    else:
        print("no", end=" ")
