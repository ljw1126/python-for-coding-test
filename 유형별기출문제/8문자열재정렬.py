"""
입력예시 
K1KA5CB7
AJKDLSI412K4JSJ9D

출력예시 
ABCKK13
ADDIJJJKKLSS20
"""

import sys 

S = sys.stdin.readline().strip()

arrS = []
arrN = []

for i in S : 
    if i.isalpha():
        arrS.append(i)
    else : 
        arrN.append(int(i)) # 바로 더해버리면 되네 .. 

arrS.sort()

print(''.join(arrS) + str(sum(arrN)))

## 해설답안 
data = input() 
result = []
value = 0 

for x in data : 
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0 : 
    result.append(str(value))

print(''.join(result))