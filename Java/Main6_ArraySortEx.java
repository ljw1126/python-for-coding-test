package Java;

import java.util.Arrays;

// 정렬라이브러리 기본예제
public class Main6_ArraySortEx {
    public static void main(String[] args) {
        int n = 10;
        int[] array = {7,5,9,0,3,1,6,2,4,8};

        Arrays.sort(array);
        System.out.print("결과>>"+Arrays.toString(array));
    }
}
