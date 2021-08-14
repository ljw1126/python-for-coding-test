package Java;

import java.util.Arrays;
import java.util.Scanner;

/*
[문제 - 상하좌우]
- 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있습니다. 
  이 공간은 1 x 1 크기의 정사각형으로 나누어져 있습니다. 
  가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당합니다.
  여행가 A는 '상,하,좌,우 방향으로 이동'할 수 있으며, 시작 좌표는 항상 (1,1)입니다. 
  우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다. 

- 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 
  적혀 있습니다. 각 문자의 의미는 다음과 같습니다. 
  > L : 왼쪽으로 한 칸 이동
  > R : 오른쪽으로 한 칸 이동
  > U : 위로 한 칸 이동
  > D : 아래로 한 칸 이동 

- 이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다. 
  예를 들어 (1,1)의 위치에서 L혹은 U를 만나면 무시됩니다. 
  1,1 | 1,2 | 1,3
  2,1 | 2,2 | 2,3
  3,1 | 3,2 | 3,3 

 (입력조건)
 - 첫째 줄에 공간의 크기를 나타내는 N이 주어집니다. ( 1<=N<=100 )
 - 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다. ( 1 <= 이동횟수 <= 100 )

 (출력조건)
 - 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백을 기준으로 구분하여 출력합니다. 

 # 입력 예시 
    5 
    R R R U D D 

 # 출력 예시 
   3 4

--------------------
- 이 문제는 요구사항대로 충실히 구현하면 되는 문제입니다. 
- 일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 '시물레이션(Simulation) 유형'으로도 분류
  되며 구현이 중요한 대표적인 문제 유형입니다. 
  > 다만, 알고리즘 교재나 문제 풀이 사이트에 따라서 다르게 일컬을 수 있으므로 , 
    코딩 테스트에서의 시뮬레이션 유형, 구현 유형, 완전 탐색 유형은 서로 유사한 점이 많다는 정도로만 기억하면 됨
*/

public class Main4_1 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        // n x n 을 위한 n 입력 받음 
        int n = sc.nextInt();
        sc.nextLine(); // 버퍼 비우기
        String[] plans = sc.nextLine().split(" ");
        int x =1, y=1;

        //System.out.println(n);
        //System.out.println(Arrays.toString(plans));
        //System.out.printf("%d,%d", x,y);

        // 방향 백터 
        int[] dx = {-1,0,1,0};
        int[] dy = {0,-1,0,1};
        char[] moveTypes = {'U','L','D','R'};

        for(int i = 0; i < plans.length; i++){
            //System.out.println("plans[i] = " + plans[i]);
            //System.out.println("plans[i].charAt(0) = "+plans[i].charAt(0));
            char plan = plans[i].charAt(0);
            // 이동 후 좌표 구하기  , 나같은 경우 1,1을 원점으로 잡음 
            int nx = 0, ny = 0;
            for (int j = 0 ; j < moveTypes.length ; j ++){
                if(plan == moveTypes[j]){
                    nx = x + dx[j];
                    ny = y + dy[j];
                }
                //공간을 벗어나는 경우 무시
                if ( nx > n || ny > n || nx <= 0|| ny <= 0 ) continue;
                //이동 수행 
                x = nx;
                y = ny;
            }
        }

        System.out.printf("%d,%d",x,y);
    }
}
