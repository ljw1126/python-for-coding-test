

"""
2577번 - 숫자의 개수 ---------------- count() 함수 사용
문제
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

입력
첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

출력
첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
"""


# 내가 한거 
# a = int(input())
# b = int(input())
# c = int(input())

# array = [0] * 10

# for i in str(a*b*c):
#     array[int(i)] += 1
# for j in array :
#     print(j)

# 다른 사람 한거
# a = int(input())
# b = int(input())
# c = int(input())

# result = list(str(a*b*c))
# print(result)
# for i in range(10):
#     print(result.count(str(i)))

"""
10818번 최소, 최대 --------------- min(),max() 함수 통해 최소값,최대값 찾을 수 있음
문제
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
"""

# n = int(input())
# array = list(map(int, input().split()))

# print(min(array),max(array))



"""
2562번 최대값 --------- max(),min() 구한 뒤 list.index(값) 넣으면 인덱스 구해짐
문제
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.


※ numpy.argmax(), numpy.argmin() 통해서도 최대값,최소값에 대한 인덱스 구할 수 있음 
https://www.delftstack.com/ko/howto/python/get-index-of-min-and-max-value-from-list-in-python/
"""
# 내가 한거 
# array = []
# for _ in range(9):
#     array.append(int(input()))
 
# max_index = 0
# for i in range(len(array)):
#     if array[i] >= array[max_index]:
#         max_index = i+1

# print(max(array))
# print(max_index)


# array = []
# for _ in range(9):
#     array.append(int(input()))
 
# print(max(array))
# print(array.index(max(array))+1)


"""
8958번 OX퀴즈
문제
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

출력
각 테스트 케이스마다 점수를 출력한다.
"""
## 내가 한거 
# n = int(input())
# array = []

# for _ in range(n):
#     array.append(input())

# for i in range(len(array)):
#     sum = 0
#     val = 0
#     temp = list(array[i])
#     for j in range(len(temp)):
#         if j == 0 and temp[j] == 'O':
#            val += 1 
#         elif  temp[j] == 'O' or (temp[j] == 'O' and temp[j-1] == 'O'):
#            val += 1
#         else : 
#            val = 0 
#         sum += val 

#     print(sum)

## 다른사람 한거 
# n = int(input())

# for i in range(n):
#     b = input()
#     s = list(b)
#     sum = 0
#     c = 1 
#     for j in s:
#         if j == 'O':
#             sum += c 
#             c += 1
#         else :
#             c = 1
#     print(sum)


"""
3052번 나머지 ----- set() 함수를 이용해서 중복요소를 제거 가능 
문제
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

출력
첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
"""
# b = 42 
# temp = []

# for _ in range(10):
#     a = int(input())
#     temp.append(a%b)

# print(len(set(temp)))

"""
1546번 평균 

문제
세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.

세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.

출력
첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.
"""

# n = int(input()) 
# score = list(map(int,input().split()))

# max_score = max(score)
# total_score = 0

# for i in score:
#     fix_score = i/max_score * 100 
#     total_score += fix_score 

# print(total_score/n)

## 임시 []에 넣고 sum() 한뒤 구할수도 있고 
## 아래 처럼 간소화 가능 
# n = int(input()) 
# score = list(map(int,input().split()))
# total_score = 0

# for i in score:
#     total_score += i/max(score)

# print(total_score/n*100)

"""
4344번 평균은 넘겠지 ------------- slice() 잘 쓰면 됨 
문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

입력
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# 입력예시 
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

# 출력예시 
40.000%
57.143%
33.333%
66.667%
55.556%


"""

## 1.첫번째 수가 인원수, 그 뒤는 점수 
## 2.평균 구한 뒤 비율 구하기 
# 내가 한거 - 결과는 맞는데 틀렸다 함 >> 바이트 수를 줄여보자 
# c = int(input())
# score_list = []
# for _ in range(c):
#     score_list.append(list(map(int,input().split())))

# for i in range(len(score_list)):
#     mber = score_list[i][0]
#     sum = 0
#     for j in score_list[i]:
#         if j == 0 : continue
#         sum += j 
#     avg = int(sum/mber) 
#     cnt = 0 
#     for k in score_list[i]:
#         if k == 0 : 
#             continue
#         elif k >= avg : 
#              cnt += 1
#     rate = cnt/mber*100
#     print(f"{rate:.3f}%")   
## 2차로 줄였는데 틀렸음 -- 용량 403 BYTE
# c = int(input())

# for i in range(c):
#     sum = 0
#     score_list = list(map(int,input().split()))
#     for j in range(len(score_list)) :
#         if j != 0 : 
#             sum += score_list[j] 
#     avg = int(sum/score_list[0]) 
#     cnt = 0 
#     for k in range(len(score_list)) :
#         if k != 0 and score_list[k] >= avg  : 
#             cnt += 1
#     rate = cnt/score_list[0]*100
#     print(f"{rate:.3f}%")  

## 3번째 slice() 활용 ---- 300byte인데도 틀렸다함 ..   k >= avg 가 틀렸음 .. 
c = int(input())

for _ in range(c):
    score_list = list(map(int,input().split()))
    avg = int(sum(score_list[1:])/score_list[0]) 
    cnt = 0 
    for score in score_list[1:]:
        if score > avg : 
            cnt += 1
    rate = cnt/score_list[0]*100
    print(f"{rate:.3f}%")  