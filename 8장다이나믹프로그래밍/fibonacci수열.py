# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현 //시간 복잡도 O(2^n)
def fibo(x):
    if x == 1 or x == 2:
        return 1 
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

# 2. 탑다운 다이나믹 프로그래밍 소스코드  // 시간 복잡도는 O(N)
# 한번 계산된  결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100 

# 재귀함수로 구현 ( 탑다운 다이나믹 프로그래밍)
def fibo(x):
    print('f(' + str(x) + ')' , end = ' ')
    # 종료조건 ( 1 혹은 2일때 초기값 1 리턴 )
    if x == 1 or x == 2:
            return 1 
    # 이미 계산한 적 있는 문제라면 그대로 반환    
    if d[x] != 0:
        return d[x]
    # 계산한적 x 경우 점화식에 따라서 피보나치 결과 반환 
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))



# 3. 보텀엄 방식  // 시간 복잡도는 O(N)
d = [0] * 100 

d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수를 반복문으로 구현한 보텀업 다이나믹 프로그래밍 
for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])