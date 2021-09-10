"""
백준 18406
https://www.acmicpc.net/problem/18406
"""
import sys 
nums = [int(i) for i in str(sys.stdin.readline().strip())]
n = len(nums)
mid = (n - 1) // 2

if sum(nums[:mid+1]) == sum(nums[mid+1:n]):
    print("LUCKY")
else:
    print("READY")


## 해설답안 
n = input()
length = len(n)
summary = 0 

# 왼쪽 부분 자릿수 합 
for i in range(length//2):
    summary += int(n[i])

# 오른쪽 부분 자릿수 합 
for i in range(length//2 , length):
    summary -= int(n[i])

if summary == 0 :
    print('LUCKY')
else:
    print('READY') 

