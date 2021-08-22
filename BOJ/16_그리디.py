"""
11047번 동전 0

문제
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
"""

# n,k = map(int, input().split())
# array = []
# cnt = 0 # 필요한 동전 갯수 최소값  

# for _ in range(n):
#     array.append(int(input()))

# for i in array[::-1]:
#     if k // i != 0 :
#         cnt += k // i      # 몫 만큼 카운트 올리고 
#         k %= i  # 나머지를 k(원)에 넣음         

# print(cnt)

"""
11399번 ATM 

문제
인하은행에는 ATM이 1대밖에 없다. 지금 이 ATM앞에 N명의 사람들이 줄을 서있다. 사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.

사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라지게 된다. 예를 들어, 총 5명이 있고, P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2 인 경우를 생각해보자. [1, 2, 3, 4, 5] 순서로 줄을 선다면, 1번 사람은 3분만에 돈을 뽑을 수 있다. 2번 사람은 1번 사람이 돈을 뽑을 때 까지 기다려야 하기 때문에, 3+1 = 4분이 걸리게 된다. 3번 사람은 1번, 2번 사람이 돈을 뽑을 때까지 기다려야 하기 때문에, 총 3+1+4 = 8분이 필요하게 된다. 4번 사람은 3+1+4+3 = 11분, 5번 사람은 3+1+4+3+2 = 13분이 걸리게 된다. 이 경우에 각 사람이 돈을 인출하는데 필요한 시간의 합은 3+4+8+11+13 = 39분이 된다.

줄을 [2, 5, 1, 4, 3] 순서로 줄을 서면, 2번 사람은 1분만에, 5번 사람은 1+2 = 3분, 1번 사람은 1+2+3 = 6분, 4번 사람은 1+2+3+3 = 9분, 3번 사람은 1+2+3+3+4 = 13분이 걸리게 된다. 각 사람이 돈을 인출하는데 필요한 시간의 합은 1+3+6+9+13 = 32분이다. 이 방법보다 더 필요한 시간의 합을 최소로 만들 수는 없다.

줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

# 입력예시 
5
3 1 4 3 2

# 출력예시 
32
"""
# 첫번째 -- 239 byte // 70 byte 로 푼 사람있음 
# n = int(input())
# array = list(map(int,input().split()))
# array.sort()
# result = 0 

# for i in range(len(array)):
#     delay_time = 0
#     for j in range(len(array[0:i+1])):
#         delay_time += array[j]

#     result += delay_time

# print(result )

# 두번째 ----- 156byte
# n = int(input())
# array = list(map(int,input().split()))
# array.sort()
# result = 0 

# for i in range(len(array)):
#     result += sum(array[0:i+1])

# print(result)
    
## sorted() : 매개변수로 들어온 이터러블한 데이터를 새로운 정렬된 리스트로 만들어 반환함 
## 다른 사람 풀이 https://www.acmicpc.net/source/11879632
# input() # 의미없는 값으로 버려버리네 
# a=t=0
# for i in sorted(map(int,input().split())):
#     a+=i
#     t+=a
# print(t)


"""
1946번 신입 사원
 -------------------- ??서류 기준 정렬하고 면접 성적을 앞에 지원자와 비교해서 갱신해가지고 출력하는걸 어떻게 알지?? 답과 문제로 추측??

 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 
 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 
 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.


- 참고 
https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%801946%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%8B%A0%EC%9E%85-%EC%82%AC%EC%9B%90
https://mong9data.tistory.com/67
"""
# import sys 
# T = int(input())
 
# for _ in range(T):
#     N = int(sys.stdin.readline())    # 지원자 숫자 
#     array = []
#     for _ in range(N):
#         array.append(list(map(int, sys.stdin.readline().split()))) # 서류심사 성적, 면적 성적
#         # lst = sorted([list(map(int,sys.stdin.readline().strip().split())) for x in range(n)],
#         #       key = lambda x:x[0])     # 문법 모르겠음 
#     array.sort()
#     Max = array[0][1]
#     cnt = 1 # 정렬된 첫 번째 사람은 선발이니 초기값 1 
#     for i in range(1, N) :
#         if Max > array[i][1]:
#             cnt +=1 
#             Max = array[i][1]
#     print(cnt)

"""
5585번 거스름돈 ---------- 쉬운문제 
-- 왜 문제설명에 1000엔있고 N 입력을 빼는걸 나는 생각한걸까.. 
-- 타로가 1000엔을 냈고 물건값이 N이였네 ..
문제
타로는 자주 JOI잡화점에서 물건을 산다. JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.

입력
입력은 한줄로 이루어져있고, 타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져있다.

출력
제출할 출력 파일은 1행으로만 되어 있다. 잔돈에 포함된 매수를 출력하시오.
"""
# N = int(input())  # N이 물건 값
# money = [500,100,50,10,5,1]
# cnt = 0 
# taro = 1000 - N    # 타로는 1000엔을 냈다네 

# for i in money:
#     if taro // i != 0 :
#         cnt += taro//i
#         taro %= i 

# print(cnt)

"""
2720번 세탁소 사장 동혁 ----------- 쉬운문제.. 3점짜리 
거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오. 거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다. 
예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.
"""

money_list = [25,10,5,1]
for _ in range(int(input())):
    C = int(input())
    change_list = [0] * 4

    for i in range(len(money_list)):
        if C // money_list[i] != 0 :
            change_list[i] = C // money_list[i]
            C %= money_list[i]

    for j in change_list:
        print(j, end = " ")     
    print() # 줄바꿈 