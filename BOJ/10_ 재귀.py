"""
10872번 팩토리얼 
"""
# def fnc_factorial(n):
#     if n == 0 : return 1 
#     return n * fnc_factorial(n-1)

# print(fnc_factorial(int(input())))


"""
10870번 피보나치 수 5
문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 n번째 피보나치 수를 출력한다.

# 입력예시 
10

# 출력예시
55
"""
# 내가 한거 
# def fnc_fibonacci(n):
#     # if n == 0  : return 0 
#     # elif n == 1 : return 1 
#     if n <=1 : return n
#     return  fnc_fibonacci(n-2) + fnc_fibonacci(n-1)

# print(fnc_fibonacci(int(input())))

# # for 문으로 하는 경우 https://ooyoung.tistory.com/115
# n = int(input())
# fibonacci = [0,1]
# for i in range(2, n+1):
#     num = fibonacci[i-1] + fibonacci[i-2]
#     fibonacci.append(num)

# print(fibonacci[n])


"""
11729 번 하노이 탑 이동 순서 ------- 재귀와 print()로 구현
문제
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

아래 그림은 원판이 5개인 경우의 예시이다.

입력
첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

출력
첫째 줄에 옮긴 횟수 K를 출력한다.

두 번째 줄부터 수행 과정을 출력한다. 
두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 
이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

# tip 
cnt 갯수 구할 때 ( 2**N -1 ) 하면 됨 
3 인 경우 7번 돌고 
4 인 경우 15범 돔 
"""
# cnt = 0 
# array = []

# def hanoi(n, x, y):
#     global cnt 
#     cnt += 1
#     if n > 1 : hanoi(n-1, x, 6-x-y)

#     array.append(list([x,y])) 
       
#     if n > 1 : hanoi(n-1, 6-x-y, y)
    
# hanoi(int(input()),1,3)
# print(cnt)
# for i in array : 
#     print(f'{i[0]} {i[1]}')

"""
2447번 별찍기 - 10 ---------------------도저히 모르겠음 
문제
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

***
* *
***
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

입력
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

출력
첫째 줄부터 N번째 줄까지 별을 출력한다. 

# 참고 
https://yeol2.tistory.com/38
"""

def stars(n):
    matrix = []
    for i in range ( 3 * len(n) ):
        if i // len(n) == 1: 
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i%len(n)] * 3)
    return list(matrix)

star = ["***", "* *", "***"]
N = int(input())
k = 0 
while N != 3 :
    N = int(N / 3)
    k += 1 

for i in range(k): 
    star = stars(star)
for j in star : 
    print(j)