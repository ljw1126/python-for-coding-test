package Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

/*
[문제 - 문자열 재정렬]
    - 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 
    이때 모든 알파벳을 오름파순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 
    이어서 출력합니다. 
    - 예를 들어 K1KA5CB7 이라는 값이 들어오면 ABCKK13을 출력합니다. 

    (입력조건)
    - 첫째 줄에 하나의 문자열 s가 주어집니다 ( 1 <= s의 길이 <= 10,000 )

    (출력조건)
    - 첫째 줄에 문제에서 요구하는 정답을 출력합니다. 

    # 입력예시1 
    K1KA5CB7

    # 출력예시1
    ABCKK13

    # 입력예시2 
    AJKDLSI412K4JSJ9D

    # 출력예시2
    ADDIJJJKKLSS20
    --------------------
    - 요구사항대로 충실히 구현하면 되는 문제임 
    - 문자열이 입력되었을때 문자를 하나씩 확인합니다. 
    > 숫자인 경우 따로 합계를 계산합니다. 
    > 알파벳의 경우 별도의 리스트에 저장합니다. 
    - 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고 , 합계를 뒤에 붙여 출력하면 정답입니다.
*/
public class Main4_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] inputData = sc.nextLine().split("");
        
       //System.out.print(Arrays.toString(inputData));
        ArrayList<String> temp = new ArrayList();
        int sum = 0;
        
        for(int i = 0 ; i < inputData.length ; i++){
            int idx = inputData[i].charAt(0); // 해당 문자 아스키 구함 
            if(48 <= idx && idx <= 57) { // 숫자인 경우
                sum += idx -'0';
            }else if(65 <= idx && idx <= 122){
                temp.add(inputData[i]);
            }
        }
        Collections.sort(temp);
        // System.out.println(temp);
        // System.out.println(String.join("",temp));
        // System.out.println(sum);
        System.out.println(String.join("",temp)+""+sum);
    }
}
