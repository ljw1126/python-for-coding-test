"""
2020 카카오 신입공채 - 하나도 모르겠음 , 답안 보고 하니 이해함 
- 생각은 절반 만큼 나눠서 .. 뭔갈 하는건 생각함 .. 
https://programmers.co.kr/learn/courses/30/lessons/60057
"""
import sys 
s = sys.stdin.readline().strip() 

answer = len(s)

for step in range(1, len(s) // 2 + 1):
    print(f'step = {step}')
    compress = ""
    prev = s[0:step]
    print(f'prev = {prev}')
    count = 1 
    # 단위(step) 크기 만큼 증가시며 이전 문자열과 비교 
    for j in range(step, len(s), step):
        # 이전 상태와 동일하다면 압축 횟수 (count) 증가 
        if prev == s[j:j+step]: 
            count += 1
        # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
        else: 
            compress += str(count) + prev if count >=2 else prev 
            prev = s[j:j+step] # 다시 상태 초기화
            count = 1 
    
    # 남아 있는 문자열에 대해서 처리 
    compress += str(count) + prev if count >= 2 else prev 
    print(f'compress = {compress}')
    answer = min(answer, len(compress))
    print(answer)
