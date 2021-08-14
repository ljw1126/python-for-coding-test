package Java;

import java.util.Scanner;

/*

# 시뮬레이션, 2차원 

[문제 - 왕실의 나이트 ]
- 행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면입니다. 
  왕실 정원의 특정한 한 칸에 나이트가 서 있습니다. 나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다. 
- 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없습니다. 
- 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다. 
  1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기 
  2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기 

- 이처럼 8 x 8 좌표 표면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 
  프로그램을 작성하세요. 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 
  a 부터 h 로 표현합니다. 
  > c2에 있을 때 이동할 수 있는 경우의 수는 6가지 입니다. 

(입력조건)
- 첫째 줄에 8 x 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 
  두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1 처럼 열과 행으로 이뤄진다. 

(출력조건)
- (첫째 줄에?) 나이트가 이동할 수 있는 경우의 수를 입력하시오.


# 입력예시 
  a1
# 출력예시 
  2 
--------------------
- 요구사항대로 충실히 구현하면 되는 문제임
- 나이트의 8가지 경로를 하나씩 확인하여 각 위치로 이동이 가능한지 확인합니다. 
  > 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의합니다. 


  ※ 아스키 코드 표 링크 >> https://blog.naver.com/PostView.nhn?blogId=jysaa5&logNo=221831226674
*/
public class Main4_3 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        //현재 나이트 위치 입력받기 
        String inputData = sc.nextLine();
        int row = inputData.charAt(1) - '0';  //아스키 모르겠다..
        int col = inputData.charAt(0) - 'a' + 1;

        //System.out.println(row);
        //System.out.println(col);

        // 나이트가 이동 할 수 있는 8가지 방향 정의
        int[] dx = {-2,-1,1,2,2,1,-1,-2};
        int[] dy = {-1,-2,-2,-1,1,2,2,1};
  

        int result = 0;
        for (int i=0; i< 8; i++){
            // 이동하고자 하는 위치 확인 
            int nextRow = row + dx[i];
            int nextColumn = col + dy[i];

            if( nextRow >=1 && nextRow <= 8 && nextColumn >=1 && nextColumn <= 8 ) result++;
        }   
        
        System.out.println("result = " + result);

    }
}
