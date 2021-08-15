package Java;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

/*
 [위에서 아래로]
 - 하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있습니다. 
   이 수를 큰 수버터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

 [입력조건]
 - 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다 ( 1 <= N <= 500)
 - 둘째 줄부터 N+1 번째 줄까지 N개의 수가 입력된다. 수의 범위는 1이상 100,000 이하의 자연수 이다. 
 
 [출력조건]
 - 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 
   동일한 수의 순서는 자유롭게 출력해도 괜찮다.

 # 입력예시 
   3
   15
   27
   12
 # 출력예시
   27 15 12  

*/
 public class Main6_exam1 {
    public static void main(String[] args) {
        // 내 소스
        Scanner sc = new Scanner(System.in);
        // N을 입력받기 
        int n = sc.nextInt();
        sc.nextLine();

        Integer[] array = new Integer[n];
        for(int i=0 ; i < n ; i++){
            array[i] = sc.nextInt();
        }

        // 기본 정렬 라이브러리를 이용하여 내림차순 정렬 
        Arrays.sort(array, Collections.reverseOrder());

        for(int num : array){
            System.out.print(num + " ");
        }

    }
}
