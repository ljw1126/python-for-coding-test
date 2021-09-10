
#### String 입력받아 정수형 리스트 변환
```
A = list(map(int, input().split()))       // map 없이 하면 string으로 들어감 

# 입력 
1 10 4 9 2 3 8 5 7 6
# 출력
[1, 10, 4, 9, 2, 3, 8, 5, 7, 6]
```

###
```
result = list(str(a*b*c))
# 숫자 넣었을때 곱셈 결과가 리스트로 담김 
['1', '8', '4', '7', '3', '7', '0', '0']
# count 함수 통해서 해당 문자가 몇개 있는지 찾을 수 있음 
for i in range(10):
    print(result.count(str(i)))
```  



### int를 list에 담을 떄 
```
 array = list(map(int,str(i)))
 또는 
 n = list(map(int,str(sys.stdin.readline().strip())))
 print(n)
 # 내포 표기 생성
 nums = input() # str이니깐 밑에 for문 으로 해서 넣을 수 있지  
 nums = [int(n)  for n in nums]
 # [2,3,1,4]
 ordered_nums = sorted(nums, reverse=True)
```

### sort(), sorted()
```
https://velog.io/@aonee/Python-%EC%A0%95%EB%A0%AC-sort-sorted-reverse
```

### heapq 모듈  - 최소힙, 최대힙 // 힙 정렬에도 사용되는 , 최소 합 구하는 문제 활용가능 
```
 https://www.daleseo.com/python-heapq/
```