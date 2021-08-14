package Java;

import java.util.Stack;

/*
    스택 ( Stack )
    - First In Last Out 선입후출
*/
public class Main5_Stack {
    public static void main(String[] args) {
        Stack<Integer> st = new Stack<>();

        // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) -삭제()
        st.push(5);
        st.push(2);
        st.push(3);
        st.push(7);
        st.pop();
        st.push(1);
        st.push(4);
        st.pop();

        // 스택의 최상단 원소부터 출력 
        while(!st.empty()){
            System.out.print(st.peek() + " "); // 최상단 출력 
            st.pop();
        }

        // 실행 결과 => 1 3 2 5 
    }
}
