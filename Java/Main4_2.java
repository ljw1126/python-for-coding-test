package Java;
/*

 [문제 - 시각 ]
    - 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 '모든 시각 중에서 3이 하나라도 포함되는
    모든 경우의 수를 구하는 프로그램을 작성'하세요. 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 
    있으므로 세어야 하는 시각입니다. 
    > 00시 00분 03초
    > 00시 13분 30초 
    - 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각입니다. 
    > 00시 02분 55초 
    > 01시 27분 45초 

    (입력조건)
    - 첫째줄에 정수 N이 입력됩니다. ( 0 <= N <= 23 )
    (출력조건) 
    00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력합니다. 

    # 입력 예시 
    5

    # 출력 예시
    11475  

    --------------------
    - 이 문제는 '가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제'입니다.
    - 하루는 86,400초이므로, 00시 00분 00초부터 23시 59분 59초까지의 모든 경우는 86,400가지 입니다. 
    > 24 * 60 * 60 = 86,400    // ※ 파이썬은 1초에 2천만번 연산 수행한다고 가정하면됨 
    - 따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지를 확인하면 됩니다. 
    - 이러한 유형은 '완전 탐색(Brute Forcing)' 문제 유형이라고 불립니다. 
    > 가능한 경우의 수를 모두 검사해보는 탐색 방법을 의미함 
*/

import java.util.Scanner;

public class Main4_2 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        // 00 시 00분 00초 ~ n시 59분 59초 
        int h = sc.nextInt();
        sc.nextLine();
        
        int cnt = 0 ;

        // 매 시각 안에 '3' 포함되어 있는 경우 카운터 증가 
        for(int i=0; i <= h; i++){
            for(int j=0;j<60;j++){
                for(int k=0;k<60;k++){
                   if(check(i,j,k)) cnt++;
                }
            }
        }

        System.out.println("결과(cnt) >>"+cnt);
    }

    public static boolean check(int h, int m ,int s){

        if( h%10 == 3 || h/10 ==3 || m%10 == 3 || m/10 == 3 ||s%10 == 3 || s/10 == 3 ) return true;

        return false;
    }

}
