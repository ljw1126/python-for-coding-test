"""
https://programmers.co.kr/learn/courses/30/lessons/60059
>> 답안 봐도 이해 안됨..
3
0 0 0
1 0 0 
0 1 1
3
1 1 1
1 1 0
1 0 1
"""
import sys 
key = [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
lock = [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
