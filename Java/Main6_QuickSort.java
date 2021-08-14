package Java;

import java.util.Arrays;

// [퀵 정렬]
public class Main6_QuickSort {
    public static int[] array = {5,7,9,0,3,1,6,2,4,8};
    public static void main(String[] args) {
        quickSort(array, 0, array.length-1);
        System.out.print("결과>>"+Arrays.toString(array));
    }

    public static void quickSort(int[] array , int start , int end){
        
        if(start >= end) return; 

        int pivot = start; 
        int left = start + 1;
        int right = end;

        while(left <= right){
             
             //pivot 보다 큰값을 찾을 때까지 left(인덱스) 증가    
             while( left <= end && array[left] <= array[pivot] ) left++;
              
             //pivot 보다 작은 값을 찾을 때까지 right(인덱스) 감소 
             while( right > start && array[right] >= array[pivot]) right--;

             // left < right 인 경우 정상 스왑              
             if(left < right){
                int temp = array[left];
                array[left] = array[right];
                array[right] = temp;
             }else{ // left > right
                int temp = array[pivot];
                array[pivot] = array[right];
                array[right] = temp; 
             }
             // left > right 인 경우 pivot과 right 스왑 
        }
        
        // 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quickSort(array, start, right -1);
        quickSort(array, right+1, end);
    }
}
