"""
10828번 스택
문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
------------------

- 파이썬은 스택 자료구조는 따로 제공 x
- list 사용해서 스택 흉내 낼 수 있음 
- *.append()    // ,push
- *.pop()       // 리스트의 가장 마지막 원소 제거,pop
- 배열[-1]      // 스택에서 원소 제거하지 않고 마지막 원소 가져올때 , top
"""

# def stack_func(stack, cmd):
#     if cmd[0] == "push":
#         stack.append(cmd[1])
#     elif cmd[0] == "top":
#         if len(stack) == 0 : 
#             print(-1)
#         else:
#             print(stack[-1])
#     elif cmd[0] == "size":
#         print(len(stack))
#     elif cmd[0] == "pop":
#         if len(stack) == 0 : 
#             print(-1)
#         else :
#             print(stack.pop())   
#     elif cmd[0] == "empty":
#         stack = []
#         print(len(stack)) 

# n = int(input())
# stack = []

# for _ in range(n):
#     stack_func(stack, list(input().split()))

# 2번째 ---------- 500 byte  // 172 byte 어떻게 하는거지?
# input() 쓰면 시간초과 되므로 sys 라이브러리 사용 
# empty를 잘못 읽음.. try, except: 문 지움 
# 참고 : https://velog.io/@wjdtmdgml/%EB%B0%B1%EC%A4%80%EC%8A%A4%ED%83%9D10828%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EC%8A%A4%ED%83%9D
# import 하고 600byte까지 올라갔지만 통과..
# import sys 

# stack = []
# for _ in range(int(sys.stdin.readline())):
#         cmd = sys.stdin.readline().split()    # 리스트로 담김 
#         if cmd[0] == "push":
#             stack.append(int(cmd[1])) 
#         elif cmd[0] == "pop":
#             if len(stack) > 0 : 
#                 print(stack.pop())   
#             else :
#                 print(-1)
#         elif cmd[0] == "size":
#             print(len(stack))
#         elif cmd[0] == "empty":    # 요거 0,1 바껴있었음 
#             if len(stack) > 0 :
#                 print(0)
#             else : 
#                 print(1)
#         elif cmd[0] == "top":
#             if len(stack) > 0 : 
#                 print(stack[-1])
#             else : 
#                 print(-1)    

"""
10773번 제로 -----------통과
문제
나코더 기장 재민이는 동아리 회식을 준비하기 위해서 장부를 관리하는 중이다.

재현이는 재민이를 도와서 돈을 관리하는 중인데, 애석하게도 항상 정신없는 재현이는 돈을 실수로 잘못 부르는 사고를 치기 일쑤였다.

재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.

재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!

입력
첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)

이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.

정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

출력
재민이가 최종적으로 적어 낸 수의 합을 출력한다. 최종적으로 적어낸 수의 합은 231-1보다 작거나 같은 정수이다.
"""
# import sys 
# stack = []
# for _ in range(int(sys.stdin.readline())):
#     cmd = int(sys.stdin.readline())
#     if cmd == 0 : 
#         stack.pop()
#     else:
#         stack.append(cmd)

# print(sum(stack))

"""
9012번 괄호 
문제
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

출력
출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 
"""
# count로 풀려했는데 아닌 듯, stack 문제니 append , pop 이런걸로.. 
# import sys 

# for _ in range(int(sys.stdin.readline())):
#     stack = []
#     array = sys.stdin.readline()
#     for i in array :
#         stack.append(i)

#     print(stack.count(")"), stack.count("("))

## stack 문제니  참고해서 풀었는데.. https://j-ungry.tistory.com/182
import sys 

for _ in range(int(sys.stdin.readline())):
    stack = []
    txt = sys.stdin.readline().strip()   ## ()()()()(()()())() 공백 들어가서 헛 print("NO") 출력됨 
    check = True
    for i in txt : 
        if i == "(":
            stack.append(i)
        else :  # "("인 경우  
            if len(stack) > 0 :
                stack.pop(-1)  # pop() 해도 되고 , 인덱스 지정해도 되고 
            else : 
                print("NO")
                check = False
                break
    
    # stack 에는 pop 하지 못한게 있거나, 아니면 [] 인 상태 출력됨
    if check == True and len(stack) != 0:
        print("NO")
    elif check == True and len(stack) == 0:
        print("YES")

       
"""
1. 오류 상황  
(()((())()(
['(', '(']
True
NO가 출력되야함 
2. 오류 
()()()()(()()())()
NO
[]
False
>>  txt = sys.stdin.readline().strip()   공백이 들어가서 반복문 돌아서 에러남 
"""