package Java;

import java.util.Scanner;

/*
    [1일 될 때까지]

    [문제]
        - 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다.
        단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있습니다. 

        1. N에서 1을 뺍니다. 
        2. N을 K로 나눕니다. 

        - 예를 들어 N이 17, K가 4라고 가정합시다. 이때 1번의 과정을 한 번 수행하면 N은 16이 됩니다. 
        이후에 2번의 과정을 두 번 수행하면 N은 1이 됩니다. 결과적으로 이 경우 전체 과정을 실행한 
        횟수는 3이 됩니다. 이는 N을 1로 만드는 최소 횟수입니다. 

        - N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는
        프로그램을 작성하세요. 

        (입력조건) 
        - 첫째 줄에 N( 1<=N<=100,000)과 K(2<=K<=100,000)가 공백을 기준으로 하여 각각 자연수로 주어집니다.

        (출력조건)
        - 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력합니다.

        --------------------
        - 주어진 N에 대하여 '최대한 많이 나누기'를 수행하면 됨 
        - N의 값을 줄일때 '2이상의 수로 나누는 작업'이 '1을 빼는 작업보다' 수를 훨씬 많이 줄일 수 있습니다.

*/
public class Main3_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    
        // N, K 를 공백 기준으로 구분하여 입력받기 
        int n = sc.nextInt();
        int k = sc.nextInt();
        int result = 0 ;
        // 1. 내가 한거 
        // while( n > 1 ){

        //     if( n % k == 0 ){
        //         n /= k;
        //     }else{
        //         n -= 1;
        //     }
        //     result++;
        // }
        // System.out.println(n);
        // System.out.println(result);
        
        // 2. 해설답안 
        while(true){

            int target = (n/k) * k;
            result += (n-target); // - 할 값을 미리 구하네 
            n = target;
           
            if ( n < k ) break; 

            n /= k;
            result += 1;
        } 
        // 마지막으로 남은 수에 대하여 1씩 빼기 (..?)
        result += (n-1);
        System.out.println(result);

    }
}
