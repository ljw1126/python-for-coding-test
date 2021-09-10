"""
백준 1715 번 - 카드 정렬하기
https://www.acmicpc.net/problem/1715

#입력예시 
3
10
20
40
#출력예시 
100
"""
# 재귀로도 반복문으로도 못 품 .. 
# '항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해를 보장함'
# heapq 모듈 사용시 최소힙을 보장함 
# heapq 모듈 참고 > https://www.daleseo.com/python-heapq/
# 해설답안
import sys 
import heapq

heap = []
# 데이터 입력시 오름차순으로 입력한다고 가정 
for i in range(int(sys.stdin.readline())):
    heapq.heappush(heap, int(sys.stdin.readline()))

result = 0 

while len(heap) != 1 : 
       print(f'heap = {heap}')
       one = heapq.heappop(heap)
       two = heapq.heappop(heap)

       sum_value = one + two 
       result += sum_value 
       heapq.heappush(heap, sum_value) 

print(result)