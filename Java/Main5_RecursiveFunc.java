package Java;
/*
    재귀함수 ( RecursiveFunction )
    - 자기 자신을 다시 호출하는 함수 
*/
public class Main5_RecursiveFunc {
    public static void main(String[] args) {
        // 1 단순 재귀 무한 호출 
        //recursiveFunc();
        
        // 2 종료조건 명시한 재귀함수
        //recursive_function(1);

        // 3 팩토리얼 
        System.out.println("반복적으로 팩토리얼 구현 = "+factorialIterative(5));
        System.out.println("재귀적으로 팩토리얼 구현 = "+factorialRecursive(5));
    }
    
    // 1.단순 재귀 호출 예시 
    public static void recursiveFunc(){
        System.out.println("재귀 함수를 호출합니다.");
        recursiveFunc();
    }
    
    // 2.종료조건 명시 예시 
    public static void recursive_function(int i){
        if ( i == 100 ) return ;
        System.out.printf("%d 번째 재귀함수에서 %d 번째 재귀함수를 호출합니다.\n",i,i+1);
        recursive_function(i+1);
        System.out.printf("%d 번째 재귀함수를 종료합니다.\n",i);
    }

    // 3-1. 반복적으로 구현한 팩토리얼 
    public static int factorialIterative(int n){
        int result = 1;
        // 1부터 n까지의 수를 차례대로 곱하기 
        for ( int i=1 ; i<=n ; i++){
            result *= i ;
        }
        return result;
    } 
    // 3-2. 재귀적으로 구현한 팩토리얼
    public static int factorialRecursive(int n){
        // n이 1이하인 겨웅 1을 반환 
        if ( n <= 1) return 1;
        // n! = n * (n-1)! 를 그대로 코드로 작성하기 
        return n * factorialRecursive(n-1) ;
    }



}
