package Java;

import java.util.Scanner;

/**
 * 이진 탐색 - 재귀함수 사용
    # 입력예시1 
        10 7
        1 3 5 7 9 11 13 15 17 19    
    # 출력예시1
        4

    # 입력예시2 
        10 7
        1 3 5 6 9 11 13 15 17 19    
    # 출력예시2
        원소가 존재하지 않습니다. 
 */
public class Main7_binarySearch {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       
       // 원소의 개수(n)와 찾고자 하는 값(target)을 입력받기 
       int n = sc.nextInt();
       int target = sc.nextInt();

       // 전체 원소 입력받기 
       int[] arr = new int[n];
       for(int i=0; i < arr.length ; i++){
           arr[i] = sc.nextInt();
       } 

       // 이진 탐색 수행 결과 출력 
       int result = binarySearch_for(arr, target, 0, n-1);
    
       if ( result == -1 ){
           System.out.println("원소가 존재하지 않습니다.");
       }else{
           System.out.println(result + 1);
       }

    }
    // 1.재귀적으로 이진 탐색 구현 
    public static int binarySearch_Recrusive(int[] arr, int target, int start, int end){
        if ( start > end ) return -1;
        // 중간 인덱스 구함
        int mid = (start + end )/2;
        // 중간값과 찾는 값이 같은 경우 
        if (arr[mid] == target) return mid;
        // 중간값이 찾는 값보다 큰 경우 왼쪽 확인
        else if (arr[mid] > target) return binarySearch_Recrusive(arr,target,start,mid-1);
        // 중간값이 찾는 값보다 작은 경우 오른족 확인 
        else return binarySearch_Recrusive(arr,target,mid+1,end);
    }

    public static int binarySearch_for(int[] arr, int target, int start , int end){

        while(start <= end){


            int mid = (start + end ) / 2;
            // 찾은 경우 중간점 인덱스 반환
            if (arr[mid] == target ) return mid;
            // 중간점 값보다 찾는 값이 작은 경우 왼쪽 확인
            else if(arr[mid] > target) end = mid - 1;
            // 중간점 값보다 찾는 값이 큰 경우 오른쪽 확인
            else start = mid + 1;
        }    

        return -1;
    }
}