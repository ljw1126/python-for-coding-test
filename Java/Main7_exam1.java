package Java;

import java.util.Scanner;

/*

[떡볶이 떡 만들기]  >> https://youtu.be/jjOmN2_lmdk

(문제설명)
    - 오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했습니다. 
      오늘은 떡볶이 떡을 만드는 날입니다. 동빈이네 떡볶이 떡은 재밌게도 떡볶이의 떡의 길이가 일정하지 않습니다.
      대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줍니다. 
    - 절단기에 '높이(H)'를 지정하면 줄지어진 떡을 한 번에 절단합니다. 
      높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않습니다. 
    - 예를 들어 높이가 19,14,10,17cm 인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의
      높이는 15,14,10,15cm 가 될 것입니다. 잘린 떡의 길이는 차례대로 4,0,0,2cm 입니다. 
      손님은 6cm 만큼의 길이를 가져갑니다. 
    - 손님이 왔을 때 요청한 총 길이가 M일 때 '적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 
      높이의 최대값을 구하는 프로그램'을 작성하세요.

(입력조건)
    - 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어집니다. 
      ( 1 <= N <= 1,000,000 , 1 <= M <= 2,000,000,000 )
    - 둘째 줄에는 떡의 개별 높이가 주어집니다. 떡 높이의 총합은 항상 M 이상이므로, 손님의 필요한 양만큼
      떡을 사갈 수 있습니다. 높이는 10억보다 작거나 같은 양의 정수 또는 0 입니다. 

(출력조건)
    - 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력합니다. 

# 입력예시 
    4 6
    19 15 10 17

# 출력예시 
    15

*/
public class Main7_exam1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 떡의 개수(n)와 요청한 떡의 길이(M)
        int n = sc.nextInt();
        int m = sc.nextInt();

        // 각 떡의 개별 높이 정보 
        int[] arr = new int[n];
        for(int i=0; i < arr.length ; i++){
            arr[i] = sc.nextInt();
        }

        // 이진 탐색을 위한 시작점과 끝점 설정 
        int start = 0;
        int end = (int)1e9; // e의 의미는 10의 제곱 
        int result = 0 ;

        while ( start <= end ){
            int h = (start + end)/2;   // 높이 h 
            int total = 0;

            for(int num : arr){
                if ( num > h ){
                    total +=  num - h;
                }
            }
            
            // 자른 값이 구하려는 m 보다 큰 경우 
            if (total >= m ){
                start = h + 1;
                result = h;
            }else{ // 자른 값이 구하려는 m 보다 작은 경우 
                end = h - 1;
            }
        }

        System.out.println(result);
    }
}
