
"""
# 시뮬레이션, 2차원 

[문제]
- 행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면입니다. 
  왕실 정원의 특정한 한 칸에 나이트가 서 있습니다. 나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다. 
- 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없습니다. 
- 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다. 
  1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기 
  2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기 

- 이처럼 8 x 8 좌표 표면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 
  프로그램을 작성하세요. 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 
  a 부터 h 로 표현합니다. 
  > c2에 있을 때 이동할 수 있는 경우의 수는 6가지 입니다. 

(입력조건)
- 첫째 줄에 8 x 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 
  두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1 처럼 열과 행으로 이뤄진다. 

(출력조건)
- (첫째 줄에?) 나이트가 이동할 수 있는 경우의 수를 입력하시오.


# 입력예시 
  a1
# 출력예시 
  2 
--------------------
- 요구사항대로 충실히 구현하면 되는 문제임
- 나이트의 8가지 경로를 하나씩 확인하여 각 위치로 이동이 가능한지 확인합니다. 
  > 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의합니다. 


"""
# 내가 한거 
import time 
point = list(input())
start_time = time.time()
count = 0 

col = ['a','b','c','d','e','f','g','h']
d_row = [2,2,-2,-2,1,-1,1,-1]
d_col = [1,-1,1,-1,2,2,-2,-2]

for i in range(len(col)):
    if col[i] in point[0]: x,y = int(point[1]),int(i + 1) 
#print(f"{x},{y}")
for i in range(len(d_row)):
    dx = x + d_row[i]
    dy = y + d_col[i]
    #print(f"{dx} , {dy}")
    if dx < 0 or dy < 0 or dx > 8 or dy > 8 : 
        continue

    count += 1    

print(count)
end_time = time.time()  # 측정 종료
print("time:", end_time - start_time) #수행 시간 출력 



# 해설 답안 
# 현재 나이트의 위치 입력받기 
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1      # 아스키 코드로 구할 수 있구나 

# 나이트가 이동할 수 있는 8가지 방향 정의 
steps = [(-2,-1),(-2,1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2)]

# 8가지 방향에 대하여 각 우치로 이동이 가능한지 확인 
result = 0 
for step in steps:
    # 이동하고자 하는 위치 확인 
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동 가능하면 카운트 증가 
    if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <=8:
        result +=1 


print(result)
