"""
문제)
당신은 음식점의 계산을 도와주는 점원입니다. 
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정합니다.
손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수를 구하세요.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다. 


- 최적의 해를 빠르게 구하기 위해서는 '가장 큰 화폐 단위부터' 돈을 거슬러주면 됨
- N원을 거슬러 줘야 할 때, 가장 먼저 500원으로 거슬러 줄 수 있을 만큼 거슬러 줍니다. 
  > 이후에 100원, 50원, 10원짜리 동전을 차례대로 거슬러 줄 수 있을 만큼 거슬러 주면 됩니다. 
- N = 1,260 일때의 예시를 확인해 봅니다. 

"""

import time 
start_time = time.time()


n = int(input()) # 거스름돈 
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500,100,50,10]

for coin in array:
    count += n // coin    # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기 
    n %= coin

print(count)

end_time = time.time()  # 측정 종료
print("time:", end_time - start_time) #수행 시간 출력 



"""
- 가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유는?
    > 가지고 있는 동전 중에서 ' 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 
       다른 해가 나올 수 없기 떄문'입니다. 
- 만약에 800원을 거슬러 주어야 하는데 화폐 단위가 500원, 400원, 100이라면 어떻게 될까요?

[시간 복잡도 분석]
- 화폐의 종류가 K 라고 할 때, 소스코드의 시간 복잡도는 O(K)입니다. 
- 이 알고리즘의 시간 복잡도는 거슬러줘야 하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받습니다.
"""