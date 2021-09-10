"""
2750번 수 정렬하기 
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

//시간 복잡도가 O(n²)인 정렬 알고리즘으로 풀 수 있습니다. 
예를 들면 삽입 정렬, 거품 정렬 등이 있습니다.  // 선택 정렬 추가 

"""

# array = []

# for _ in range(int(input())):
#     array.append(int(input()))

# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j-1]:
#             array[j],array[j-1] = array[j-1],array[j]
#         else:
#             break 

# for k in array:
#     print(k)

"""
10989번 수 정렬하기 3 -- 계수정렬 사용하기 
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
# 메모리 초과 에러 뜸 , 8MB 메모리를 요하네, count 배열 초기화할때 N대신 10001 하니 통과
# import sys

# N = int(sys.stdin.readline()) # input()대신 사용
# count = [0] * 10001   # N으로 했는데.. 메모리 초과라서, 메모이제이션 적용

# for i in range(N):
#     count[int(sys.stdin.readline().strip())] += 1

# for j in range(10001): # N 대신 그냥 10001 넣음
#     if count[j] != 0 :
#        for _ in range(count[j]): 
#            print(j)

"""
2751번 수 정렬하기 2 
-- 시간 복잡도가 O(nlogn)인 정렬 알고리즘으로 풀 수 있습니다. 
-- 예를 들면 병합 정렬, 힙 정렬 등이 있지만, 어려운 알고리즘이므로 지금은 언어에 내장된 정렬 함수를 쓰는 것을 추천드립니다.
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""

# import sys 

# array = []

# for _ in range(int(sys.stdin.readline())):
#     array.append(int(sys.stdin.readline().strip()))

# array.sort()

# for i in array:
#     print(i)

# ## 다른 사람 한거 1
# import sys

# N = int(sys.stdin.readline());
# print('\n'.join(map(str, sorted([int(sys.stdin.readline()) for _ in range(N)])))) # 멋지네 

# ## 다른 사람 답안 2
# from sys import stdin, stdout

# input() # 걍 버리네 
# arr = sorted(map(int, stdin.read().split())) # sorted() 사용한게 눈에 띔 
# stdout.write('\n'.join(map(str,arr)))

"""
1427번 소트인사이드
문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

입력
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
"""

# import sys 

# n = list(map(int,str(sys.stdin.readline().strip())))
# n.sort(reverse=True)

# for i in n : 
#     print(i,end='')

# # 다른 사람 해결 방법 
# nums = input() # str이니깐 밑에 for문 으로 해서 넣을 수 있지 .. 
# nums = [int(n)  for n in nums] # 내포 표기 생성 방법

# ordered_nums = sorted(nums, reverse=True)

# for n in ordered_nums : 
#     print(n, end="")

"""
11650번 좌표 정렬하기
문제
2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, 
x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. 
(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
"""
# 내 답안
# import sys

# array = []
# for _ in range(int(input())):
#     array.append(list(map(int,sys.stdin.readline().split())))

# array.sort(key=lambda x : (x[0], x[1])) # 요건 찾아봄

# for i in array : 
#     for j in i : 
#         print(j, end = ' ')
#     print()
"""
11651번 좌표 정렬하기 2 
문제
2차원 평면 위의 점 N개가 주어진다. 
좌표를 y좌표가 증가하는 순으로, 
y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
"""
# 위에 문제랑 동일, 정렬만 다름 
# import sys

# array = []
# for _ in range(int(input())):
#     array.append(list(map(int,sys.stdin.readline().split())))

# array.sort(key=lambda x : (x[1], x[0])) # 요건 찾아봄

# for i in array : 
#     for j in i : 
#         print(j, end = ' ')
#     print()    

"""
1181번 단어 정렬
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
"""
# 아직 못 품 
# import sys 

# array = []

# for _ in range(int(sys.stdin.readline())):
#     array.append(sys.stdin.readline().strip())
# # 길이로 비교하고, 그 다음 알파벳 순서로 비교하고 
# # for i in range(len(array)):
# #     min = i 
# #     for j in range(i+1, len(array)):
# #         if len(array[j]) < len(array[j-1]):
# #             min = j 
# #     array[i],array[min] = array[min],array[i]    
    
# # print(array)
"""
2108번 통계학 ------------ Counter 찾아봄 

문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.

"""

# import sys 
# from collections import Counter
# n = int(input())
# nums = [ int(sys.stdin.readline()) for _ in range(n)]

# array = sorted(nums)

# # 1. 산술평균 ( round() 풀이 가능 )
# print(f'{sum(array)/len(array):.0f}') # 소수점 첫째자리에서 반올림 ( .1f 는 두번째에서 반올림후 첫째까지 표시)
# # 2. 중앙값
# print(array[len(array)//2])
# # 3. 최빈값 // list로 구할 수 있으나, 시간초과 발생한다함 https://jiwon-coding.tistory.com/8
# # 공식 문서 https://docs.python.org/3/library/collections.html#collections.Counter
# # print(Counter(array)) # Counter({-2: 1, 1: 1, 2: 1, 3: 1, 8: 1})
# cntr = Counter(array).most_common()  # [(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)] 배열에 튜플(iterable, 반복가능) 형태로 반환 

# if len(cntr) > 1 and cntr[0][1] == cntr[1][1]:
#     print(cntr[1][0])
# else:
#     print(cntr[0][0])

# # 4. 범위 
# print(f'{max(array)-min(array)}')

"""
1026번 보물 

문제
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.

길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

S = A[0]×B[0] + ... + A[N-1]×B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다. N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

출력
첫째 줄에 S의 최솟값을 출력한다.

파이썬 공식문서
https://docs.python.org/ko/3/tutorial/datastructures.html
"""
# import sys 

# N = int(sys.stdin.readline())

# # 최대값에 a의 최소값이 차례대로 맵핑되도록 {1, 1, 0, 1, 6} 으로 만들어야 함 
# a = list(map(int,sys.stdin.readline().split())) # 오름차순 정렬  
# b = list(map(int,sys.stdin.readline().split()))
# result = 0 

# for _ in range(N):
#     result += max(b) * min(a)
#     b.pop(b.index(max(b)))       # 너무 어렵게 생각했다.
#     a.pop(a.index(min(a)))

# print(result)  

"""
2693번 N번째 큰 수 ----------- 아주 쉬움
문제
배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.

배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 <= T <= 1,000)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 배열 A의 원소 10개가 공백으로 구분되어 주어진다. 이 원소는 1보다 크거나 같고, 1,000보다 작거나 같은 자연수이다.

출력
각 테스트 케이스에 대해 한 줄에 하나씩 배열 A에서 3번째 큰 값을 출력한다.
"""

# import sys 

# N = int(sys.stdin.readline())

# for _ in range(N):
#     array = sorted(list(map(int,sys.stdin.readline().split())), reverse= True)
#     print(array[2])

"""
10814번 나이순 정렬
나이순 정렬
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
3 초	256 MB	52964	22555	17099	41.901%
문제
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

출력
첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

※ stable sort와 unstable sort 에 대해 
※ sort() 함수의 경우 최고 O(n) 시간복잡도를 갖고, stable함 
※ https://velog.io/@1204jh/10814 

"""
# stable , unstable sort 개념이 안잡혀서 어려웠음 
# 틀렸다함 
# import sys

# N = int(sys.stdin.readline())
# array = [list(sys.stdin.readline().split()) for _ in range(N)]

# array.sort(key=lambda x : (x[0]))

# for i in array : 
#     print(int(i[0]), i[1])

# import sys 

# array = [] 

# for _ in range(int(sys.stdin.readline())):
#     age, name = map(str, sys.stdin.readline().split())
#     array.append((int(age), name)) # 넣을때 int를 해줘야 하는 구나 

# array.sort(key = lambda x : x[0])

# for i in array : 
#     print(i[0], i[1])


"""
1181번 단어 정렬
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

# 중복 제거 방법1 , 
https://blockdmask.tistory.com/543

## 정렬 방법 
https://cocook.tistory.com/8

"""
# 찾아보고 직접 품 
# import sys 

# N = int(sys.stdin.readline())
# array = [sys.stdin.readline().strip() for _ in range(N)]
# result = [] # 중복 제거 리스트 

# # set() 사용시 순서 보장 x , 딕셔너리 사용해도 중복 제거 가능
# for i in array : 
#     if i not in result : 
#         result.append(i)

# for i in sorted(result, key = lambda x : ( len(x), x) ): # 두번째 인자 위해 괄호만 하면 되는데..
#     print(i)

"""
18870번 좌표 압축 --- 정렬 카테고리 문제인데.. 인덱스를 유추 못함..

문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

## 힌트 
https://gudwns1243.tistory.com/52

dict 중복제거 
https://blockdmask.tistory.com/543

## 참고 
list.index(i) 형태의 시간 복잡도 = O(N) >> 시간 초과 발생함 
index[i] 형태의 시간 복잡도 = O(1)
"""

import sys
N = int(sys.stdin.readline())

array = list(map(int,sys.stdin.readline().split()))
#uniq_arr = sorted(set(array))

# list.index(i) 사용시 시간복자도 O(N) 을 가짐 > 최대 1,000,000 수행되므로 시간초과 
# for i in array : 
#     print(uniq_arr.index(i), end=' ')
# array.sort()
# dict_array = list(dict.fromkeys(array))      # 중복제거 방법 

array2 = sorted(list(set(array)))
dict_arr = { array2[i] : i for i in range(len(array2))} # {-10: 0, -9: 1, 2: 2, 4: 3}

for i in array:
    print(dict_arr[i] , end = ' ')

## 다른 사람 답변 

N = input()
ZIP = dict()
X = list(map(int, input().split()))

v = 0
for k in sorted(X):
    
    if k not in ZIP.keys():
        ZIP[k] = v
        v += 1
    
print(' '.join(str(ZIP[x]) for x in X))