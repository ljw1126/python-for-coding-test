array = [5,7,9,0,3,1,6,2,4,8]
#array = [0,1,4,7,3,9,5,8,6,2]
def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료 
        return 
    pivot = start 
    left = start + 1
    right = end 
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복 
        while(right > start and array[right] >= array[pivot]):    
            right -= 1

        print(f" left, right >> {left},{right}")
        # left와 right가 엇갈린 경우 작은 데이터와 피벗 교체 
        if ( left > right ):
            array[pivot], array[right] = array[right], array[pivot]
            # 또는 array[right], array[pivot] = array[pivot],array[right]
        else : # 엇갈리지 않은 경우 
            array[left],array[right] = array[right],array[left]
        
        print(f" array >> {array}")
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수정
    # 엇갈리게 되면 right와 pivot 이 스왑되니 right 기준으로 재 실행   
    print(f" pivot = {pivot}")
    print(f" left = {left}")
    print(f" right = {right}")
    quick_sort(array, start, right -1 )
    quick_sort(array, right + 1, end)    


quick_sort(array, 0 , len(array)-1)
print(array)

"""
최초array >> [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
 while문 ( left <= right )
    left, right >> 1,8
    array >> [5, 4, 9, 0, 3, 1, 6, 2, 7, 8]
    left, right >> 2,7
    array >> [5, 4, 2, 0, 3, 1, 6, 9, 7, 8]
    left, right >> 6,5
    array >> [1, 4, 2, 0, 3, 5, 6, 9, 7, 8]
 pivot = 0
 left = 6
 right = 5
 #while문 종료

 # start - while문
    left, right >> 1,3
    array >> [1, 0, 2, 4, 3, 5, 6, 9, 7, 8]
    left, right >> 2,1
    array >> [0, 1, 2, 4, 3, 5, 6, 9, 7, 8]
 pivot = 0
 left = 2
 right = 1
 # end - while 문 
 
 # start - while문 
    left, right >> 3,2
    array >> [0, 1, 2, 4, 3, 5, 6, 9, 7, 8]
 pivot = 2
 left = 3
 right = 2
 # end - while문 

# start - while문
    left, right >> 5,4
    array >> [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
 pivot = 3
 left = 5
 right = 4
 # end - while문 

 # start - while문
    pivot, left, right >> 6,7,9
    left, right >> 7,6
    array >> [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
 pivot = 6
 left = 7
 right = 6
 # end - while문 

 # start - while문
    pivot, left, right >> 7,8,9
    left, right >> 10,9
    array >> [0, 1, 2, 3, 4, 5, 6, 8, 7, 9]
 pivot = 7
 left = 10
 right = 9
 # end - while문
  
 # start - while문
    left, right >> 9,8
    array >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 pivot = 7
 left = 9
 right = 8
 # end - while문 


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 

"""