"""
(문제)
- 한 마을에 모험가가 N명 있습니다. 
모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데,
'공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다. 

- 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 
'공포도가 X인 모험가는 반드시 X명이상으로 구성한 모험가 그룹에 참여'해야 여행을 떠날 수 있도록 규정했습니다. 

- 동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁급합니다. N명의 모험가에 대한 정보가 주어졌을때,
'여행을 떠날 수 있는 그룹 수의 최대값'을 구하는 프로그램을 작성하세요. 

- 예를 들어 N = 5 이고, 각 모험가의 공포도가 다음과 같다고 가정합시다. 
 > 2 3 1 2 2 
- 이 경우 그룹1에 공포도가 1인 모험가를 한 명 넣고, 그룹 2에 공포도가 2인 두명을 넣게 되면 
총 2개의 그룹을 만들 수 있습니다. 
- 또한 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 떄문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다. 
   (2,3 은 버림)

(입력조건)
- 첫째 줄에 모험가의 수 N이 주어집니다. (1<=N<=100,000)
- 둘째 줄에 각 모험가의 공포도의 값을 N이하의 자연수로 주어지며,
  각 자연수는 공백으로 구분합니다. 

(출력조건)
- 여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다. 

(입력예시)
5
2 3 1 2 2
(출력예시)
2
=================================================
- 앞에서부터 공포도를 하나씩 확인하며 '현재 그룹에 포함된 모험가의 수'가 
'현재 확인하고 있는 공포도보다 크거나 같다면 이를 그룹으로 설정'하면 됨 
- 이러한 방법을 이용하면 공포도가 오름차순으로 정렬되어 있다는 점에서, 항상 최소한의 모험가의 수만
  포함하여 그룹을 결성하게 됩니다. 
  

"""

N = int(input())
mbers = list(map(int, input().split()))

mbers.sort() # 오름차순 정렬

result = 0 # 총 그룹의 수 
cnt = 0 # 현재 그룹페 포함된 모험가의 수 

for i in mbers:
    
    cnt += 1 
    if cnt >= i:
        result += 1 
        cnt += 0 

print(result) 