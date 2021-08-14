package Java;
/*
    [음료수 얼려먹기]
    https://www.youtube.com/watch?v=e7_H8SLZlHY&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=20
    https://github.com/ndb796/python-for-coding-test/blob/master/5/10.java

    [문제설명]
    - N x M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
    구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다. 
    이때 '얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성'하세요.
    다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다. 
    // 0을 한 묶으로 해서 하나로 침 
    ```
    00110
    00011
    11111
    00000
    ```

    (입력조건)
        - 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다. ( 1<=N,M<=1,000)
        - 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어집니다. 
        - 이때 구멍이 뚫려있는 부분은 0 , 그렇지 않은 부분은 1입니다. 

    (출력조건)
        - 한 번에 만들 수 있는 아이스크림의 개수를 출력합니다. 

    # 입력예시 
        4 5 
        00110
        00011
        11111
        00000
    # 출력예시 
        3

--------------------
    - 이 문제는 DFS 혹은 BFS로 해결할 수 있습니다. 
    일단 앞에서 배운대로 얼음을 얼릴 수 있는 공간이 상,하,좌,우로 연결되어 있다고 표현할 수 있으므로 
    그래프 형태로 모델링 할 수 있습니다. 
    - DFS를 활용하는 알고리즘은 다음과 같습니다. 
    1. 특정한 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 
        않는 지점이 있다면 해당 지점을 방문합니다. 
    2. 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 진행하는 과정을 반복하면,
        '연결된 모든 지점을 방문'할 수 있습니다. 
    3. 모든 노드에 대하여 1~2번의 과정을 반복하며, 방문하지 않는 지점의 수를 카운트합니다.    
*/

import java.util.Arrays;
import java.util.Scanner;

public class Main5_exam1 {

    public static int n,m;
    public static int[][] graph = new int[1000][1000];   // 조건대로라면 이거인데 , 확인 어려워서 밑에 꺼로 함 
    //public static int[][] graph;
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        // N, M 을 공백 기준으로 구분하여 입력 받기 
        n = sc.nextInt();
        m = sc.nextInt();        
        sc.nextLine();

        //graph = new int[n][m];

        // 2차원 리스트의 맵 정보 입력받기 
        for(int i=0; i<n; i++){
            String str = sc.nextLine();
            for(int j=0; j<m; j++){
                graph[i][j] = str.charAt(j) - '0';
            }
        }

        //모든 노드(위치)에 대하여 음료수 채우기
        int result = 0 ;
        for(int i=0; i < n; i++){
            for(int j=0; j < m; j++){
                if(dfs(i,j)) result += 1;
            }
        }
    
        System.out.printf("결과값 확인 = %d", result);
        //System.out.println();
        //System.out.println("graph >> " + Arrays.deepToString(graph));
    }        

    // DFS로 특정 노드를 방문하고 연결되 모든 노드들도 방문 
    // static 으로 n x m 변수가 선언되어 있음 
    public static boolean dfs(int x, int y){
        // 주어진 범위 벗어나는 경우에는 즉시 종료 
        if ( x >= n || y >= m || x < 0 || y < 0) return false; 
        
        // 현재 노드를 아직 방문하지 않는 경우 
        if ( graph[x][y] == 0 ){
            //해당 노드 방문 처리 
            graph[x][y] = 1;
            // 상좌우하 
            dfs(x-1,y);
            dfs(x,y-1);
            dfs(x+1,y);
            dfs(x,y+1);
            
            return true;
        }

        return false;
    }
}
