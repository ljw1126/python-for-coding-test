"""
(문제)
각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을때, 
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x'혹은 '+'연산자를 넣어
결과적으로 '만들어 질 수 있는 가장 큰 수를 구하는 프로그램'을 작성하세요.
단, +보다 x 를 먼저 계산하는 일반적인 방식과는 달리, '모든 연산은 왼쪽에서부터 순서대로'
이루어진다고 가정합니다. 

예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 ((((0+2) * 9 ) * 8) * 4) = 576
입니다. 또한 만들어 질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다. 
// int 는 약 21억 , but 파이썬은 수 제한 없음 


(입력조건)
-첫째 줄에 여러개의 숫자로 구성된 하나의 문자열 S가 주어집니다. (1<= S의 길이 <= 20)

(출력조건)
-첫째 줄에 만들어 질 수 있는 가장 큰 수를 출력합니다..

======================================
- 대부분의 경우 '+' 보다는 'x'가 더 값을 크게 만듭니다. 
  > 예를 들어 5+6 = 11 이고 5*6 = 30 입니다. 
- 다만 두 수 중에서 하나라도 0 혹은 1인 경우, 공합기보다는 더하기를 수행하는 것이 효율적입니다. 
- 따라서 '두 수에 대하여 연산을 수행할 떄 , 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 
  두 수가 모두 2이상인 경우에는 곱하면 정답' 입니다. 
"""



data = input()

import time 
start_time = time.time()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에 하나라도 0 또는 1인 경우, 곱하기 보다 더하기 수행 
    num = int(data[i])
    if num <= 1 or result <=1:
        result += num 
    else:
        result *= num 

print(result)


end_time = time.time()  # 측정 종료
print("time:", end_time - start_time) #수행 시간 출력 