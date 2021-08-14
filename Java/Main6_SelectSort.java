package Java;

import java.util.Arrays;

/*
    [선택정렬]

*/
public class Main6_SelectSort {

    public static int[] array = {7,5,9,0,3,1,6,2,4,8};
    public static void main(String[] args) {
        
        for(int i = 0; i < array.length; i++){
            int min_index = i; // 가장 작은 원소의 인덱스 ( 초기 0 )
            for(int j = i+1; j < array.length; j++){
                if(array[min_index] > array[j]){
                    min_index = j;  
                    // 내가 한 방법 
                    // int temp = array[min_index]; 
                    // array[min_index] = array[j];
                    // array[j] = temp;
                }   
            }
            // 스와프 
            int temp = array[i];
            array[i] = array[min_index];
            array[min_index] = temp;
        }

        System.out.print("결과(array)>>"+ Arrays.toString(array)); // 결과(array)>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
}
