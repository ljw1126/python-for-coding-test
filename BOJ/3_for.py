"""
2739번 구구단

문제
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

출력
출력형식과 같게 N*1부터 N*9까지 출력한다.

"""

# n = int(input())

# for i in range(1,10):
#     print(f"{n} * {i} = {n*i}")

"""
10950번 A+B - 3 // 

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.
"""

# n = int(input())
# array = []

# for _ in range(n):
#     array.append(list(map(int,input().split())))

# for i in array:
#     print(i[0] + i[1])


"""
8393번 합

문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.

"""

# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i

# print(sum)

"""
15552 A + B   // 입력받는거에 대한 tip이 있으니 ********
문제
본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

C++을 사용하고 있고 cin/cout을 사용하고자 한다면, cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고, endl 대신 개행문자(\n)를 쓰자. 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 사용하면 안 된다.

Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다. BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.

Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

자세한 설명 및 다른 언어의 경우는 이 글에 설명되어 있다.

이 블로그 글에서 BOJ의 기타 여러 가지 팁을 볼 수 있다.

※ 참고 주소 
해당 문제 https://www.acmicpc.net/problem/15552
https://www.acmicpc.net/board/view/22716
파이썬 
https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

"""
# import sys 

# n = int(sys.stdin.readline())
# array = []

# for _ in range(n):
#     array.append(list(map(int, sys.stdin.readline().split())))

# for i in array:
#     print(i[0] + i[1])

"""
2741번 N 찍기

문제
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
"""
# import sys
# n = int(sys.stdin.readline())

# for i in range(1,n+1):
#     print(i)


"""
2742번 기찍 N // 거꾸로 출력하는거

문제
자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
"""

# import sys 

# n = int(sys.stdin.readline())

# for i in range(n,0,-1):
#     print(i)


"""
11021번 A+B - 7 // 7번째라는 의미인듯

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

"""
# 내가 한거 
# import sys 

# n = int(sys.stdin.readline())
# array = []

# for _ in range(n):
#     array.append(list(map(int,sys.stdin.readline().split())))


# for i in range(len(array)):
#     print(f"Case #{i+1}: {array[i][0]+array[i][1]}")

# n = int(input())

# for i in range(1,n+1):
#     a,b = map(int, input().split())
#     print(f"Case #{i}: {a+b}")

"""
11022번 A+B - 8 //똑같은데 print만 다른듯 
"""
# import sys 
# t = int(sys.stdin.readline())

# for i in range(1,t+1):
#     a,b = map(int, sys.stdin.readline().split())
#     print(f"Case #{i}: {a} + {b} = {a+b}")

"""
2438번 별 찍기 - 1 
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
"""
# 내가 한거 
# n = int(input())

# for i in range(1,n+1):
#     star = ""
#     for _ in range(i):
#         star += "*"
#     print(star)

# 다른 사람 한거 
# n = int(input())

# for i in range(1,n+1):
#     print("*"*i)

"""
2439번 별 찍기 - 2  // 거꾸로 찍기 
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
"""
# 내가 한거 
# n = int(input())

# for i in range(n,0,-1):
#     print(" "*(i-1)+"*"*(n-i+1))

# 다른 사람 
# n = int(input())

# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*i)

"""
10871번 X보다 작은 수
문제
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

출력
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
"""
# 내가 작성한 소스 
n,x = map(int, input().split())
array = input().split(" ")

for i in range(n):
    if x > int(array[i]) : print(f"{array[i]}",end=" ")

# 다른 사람 
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")
