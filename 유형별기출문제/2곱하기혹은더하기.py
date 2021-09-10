"""
페북 인터뷰 --------- 직접 품 
"""
# nums = [ int(i) for i in str(input())]

import sys
nums = [ int(i) for i in str(sys.stdin.readline().strip())]
result = nums[0] 

for i in range(1, len(nums)) : 
    if result <= 1 or nums[i] <= 1 : # 해설답안 보고 조건식 수정, 1은 곱해봐야 의미 없으니 더하는게 맞지..
        result += nums[i]
    else :
        result *= nums[i]

print(result)


## 해설 답안 
data = input() 

# 첫번째 문자를 숫자로 변경하여 대입 
result = int(data[0])

for i in range(1,len(data)):
    # 두수 중 하나라도 '0' 혹은 '1' 인 경우, 곱하기보다 더하기 수행 
    num = int(data[i])
    if num <=1 or result <= 1 : 
        result += num 
    else:
        result *= num 

print(result)