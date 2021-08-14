package Java;

import java.util.Arrays;

// [계수정렬]
public class Main6_CountingSort {
    
    // 해섭 답안에서는 array의 length 로 구하지 않고 MAX_VALUE를 지정함
    public static final int MAX_VALUE = 9;
    public static void main(String[] args) {
        // 내 소스 
        int[] array = { 7,5,9,0,3,1,6,2,9,1,4,8,0,5,2 }; 
        int[] counting = new int[10];
        
        for(int num : array){
            counting[num] += 1;
        }
        System.out.println(Arrays.toString(counting));
        System.out.println("최종결과==================");
        
        for(int i=0; i < counting.length ; i++){
            for(int j = 0 ; j < counting[i]; j++ ){
                System.out.print(i + " ");
            }
        }
    }
}
