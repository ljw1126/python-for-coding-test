package Java;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

/*
 [두 배열의 원소 교체]

    (문제 설명)
        - 동빈이는 두 개의 배열 A와 B를 가지고 있습니다. 두 배열은 N개의 원소로 구성되어 있으며, 
        배열의 원소는 모두 자연수 입니다. 
        - 동빈이는 '최대 K번의 바꿔치기' 연산을 수행할 수 있는데, 
        바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말합니다.
        - 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야 합니다.
        - N,K 그리고 배열 A와 B의 정보가 주어졌을 때, 
        최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는 '배열 A의 모든 원소의 합의 최댓값을 출력'하는 프로그램을 작성하세요.
        
    (입력 조건)
        - 첫 번째 줄에 N,K가 공백을 기준으로 구분되어 입력됩니다. ( 1 <= N <= 100,000 , 0 <= K <= N )
        - 두 번째 줄에 배열 A의 원소들이 공백을 기준으로 구분되어 입력됩니다. 
        모든 원소는 10,000,000 보다 작은 자연수 입니다. 
        - 세 번째 줄에 배열 B의 원소들이 공백을 기준으로 입력됩니다. 
        모든 원소는 10,000,000 보다 작은 자연수 입니다. 

    (출력 조건)
        - 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력합니다.

    # 입력 예시
        5 3 
        1 2 5 4 3 
        5 5 6 6 5 

    # 출력 예시 
        26


 */
public class Main6_exam3 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt(); // 배열의 원소 갯수 
        int k = sc.nextInt(); // 배열 원소 바꿔치기 갯수 

        sc.nextLine();

        Integer[] a = new Integer[n];
        Integer[] b = new Integer[n];

        for(int i = 0 ; i < n ; i++ ) {
            a[i] = sc.nextInt();
        }

        for(int j = 0 ; j < n ; j++ ) {
            b[j] = sc.nextInt();
            sc.nextLine();
        }

        Arrays.sort(a); // 오름차순 정렬 
        Arrays.sort(b, Collections.reverseOrder()); // 내림차순
 
        System.out.println(Arrays.toString(a));
        System.out.println(Arrays.toString(b));

        for(int i=0 ; i < k ; i++){
            if( a[i] < b[i]){
                int temp = a[i];
                a[i] = b[i];
                b[i] = temp;
            }
            else break;
        }

        int result = 0 ; 
        // IntStrem.of(a).sum(); 으로 구하는 방법도 있음
        for( int num : a ){
            result += num;
        }

        System.out.println("최대값 >>" + result);
    }
}
