package Java;

import java.util.Arrays;

// [삽입정렬]
public class Main6_insertSort {
    public static void main(String[] args) {
        
        int[] array = {7,5,9,0,3,1,6,2,4,8};
        // i와 j 범위를 잘못 설정해서 i = 10 까지 가버림 
        for(int i=1; i < array.length; i++){
            
            // 인덱스 i부터 1까지 감소하며 반복하는 문법
            for(int j = i; j > 0 ; j--){
                // 한 칸씩 왼쪽으로 이동 
                if(array[j] < array[j-1]){
                    int temp = array[j];
                    array[j] = array[j-1];
                    array[j-1] = temp; 
                }
                // 자기보다 작은 데이터를 만나면 break;
                else break; 
            }
        }

        System.out.print("결과(array)>>" + Arrays.toString(array)); // 결과(array)>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
}
