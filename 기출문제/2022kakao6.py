"""
- 제한사항
    1 ≤ board의 행의 길이 (= N) ≤ 1,000
    1 ≤ board의 열의 길이 (= M) ≤ 1,000
    1 ≤ board의 원소 (각 건물의 내구도) ≤ 1,000
    1 ≤ skill의 행의 길이 ≤ 250,000
    skill의 열의 길이 = 6
    skill의 각 행은 [type, r1, c1, r2, c2, degree]형태를 가지고 있습니다.
    type은 1 혹은 2입니다.
    type이 1일 경우는 적의 공격을 의미합니다. 건물의 내구도를 낮춥니다.
    type이 2일 경우는 아군의 회복 스킬을 의미합니다. 건물의 내구도를 높입니다.
    (r1, c1)부터 (r2, c2)까지 직사각형 모양의 범위 안에 있는 건물의 내구도를 degree 만큼 낮추거나 높인다는 뜻입니다.
    0 ≤ r1 ≤ r2 < board의 행의 길이
    0 ≤ c1 ≤ c2 < board의 열의 길이
    1 ≤ degree ≤ 500
    type이 1이면 degree만큼 건물의 내구도를 낮춥니다.
    type이 2이면 degree만큼 건물의 내구도를 높입니다.
    건물은 파괴되었다가 회복 스킬을 받아 내구도가 1이상이 되면 파괴되지 않은 상태가 됩니다. 
    즉, 최종적으로 건물의 내구도가 1이상이면 파괴되지 않은 건물입니다.

-정확성 테스트 케이스 제한 사항
    1 ≤ board의 행의 길이 (= N) ≤ 100
    1 ≤ board의 열의 길이 (= M) ≤ 100
    1 ≤ board의 원소 (각 건물의 내구도) ≤ 100
    1 ≤ skill의 행의 길이 ≤ 100
    1 ≤ degree ≤ 100

-효율성 테스트 케이스 제한 사항
    주어진 조건 외 추가 제한사항 없습니다.

# 제출답안 1  - 효율성 테스트 실패 
def solution(board, skill):
    answer = 0

    for i in range(len(skill)):
        ty, r1, c1, r2, c2, degree = skill[i] 
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if ty == 1 :  # 공격
                    board[i][j] -= degree
                else :  # 회복
                    board[i][j] += degree

    for i in board:
        for j in i:
            if j > 0 : answer += 1 

    return answer

# 제출답안 2 - 효율성 테스트 실패 
import numpy as np
def solution(board, skill):
    answer = 0
    x = np.array(board)

    for i in range(len(skill)):
        ty, r1, c1, r2, c2, degree = skill[i] 
        if ty == 1 : # 공격
            x[r1:r2+1, c1:c2+1] -= degree 
        else: # 회복
            x[r1:r2+1, c1:c2+1] += degree 

    answer = len(x[x>0])

    return answer

"""
# 정확성 통과 , 효율성 실패 
# 테스트 케이스 1 >> result = 10이 나와야함 
# board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
# skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

# 테스트 케이스 2 >> result = 6 나와야함 ( 배열 값이 1 이상인 경우 )
board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

# for i in range(len(skill)):
#     ty, r1, c1, r2, c2, degree = skill[i] 
#     for i in range(r1,r2+1):
#         for j in range(c1,c2+1):
#             if ty == 1 :  # 공격
#                 board[i][j] -= degree
#             else :  # 회복
#                 board[i][j] += degree
               

# print(board)
# # 2차원 배열에서 0 이상인 값 카운트 
# result = 0 
# for i in board:
#     for j in i : 
#         if j > 0 : result += 1

# print(result)

### 요렇게 줄여도 정확성은 통과 (0.01ms, 10.3MB) ~ 통과 (14.79ms, 10.3MB), 효율성 실패..
for s in skill:
    for i in range(s[1],s[3]+1):
        for j in range(s[2],s[4]+1):
            if s[0] == 1 :  # 공격
                board[i][j] -= s[5]
            else :  # 회복
                board[i][j] += s[5]
               

print(board)
# 2차원 배열에서 0 이상인 값 카운트 
result = 0 
for i in board:
    for j in i : 
        if j > 0 : result += 1

print(result)

# ==========================================================
# 이것도 효율성 테스트 걸림
# 테스트 케이스 1 >> result = 10이 나와야함 
#board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
#skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

# 테스트 케이스 2 >> result = 6 나와야함 ( 배열 값이 1 이상인 경우 )
# board = [[1,2,3],[4,5,6],[7,8,9]]
# skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

# import numpy as np

# x = np.array(board)
# for i in range(len(skill)):
#     ty, r1, c1, r2, c2, degree = skill[i] 
#     if ty == 1 : x[r1:r2+1, c1:c2+1] -= degree 
#     else: x[r1:r2+1, c1:c2+1] += degree 
  
# print(x)
# print(len(x[x>0]))


# 변수 삭제하니 속도는 0.04ms 내려갔는데 메모리는 28MB 차지함 
# import numpy as np

# x = np.array(board)
# for i in skill:
#     if i[0] == 1 : x[i[1]:i[3]+1, i[2]:i[4]+1] -= i[5] 
#     else: x[i[1]:i[3]+1, i[2]:i[4]+1] += i[5] 
  
# print(x)
# print(len(x[x>0]))