package Java;

import java.util.LinkedList;
import java.util.Queue;

/*
    큐(Queue)
    - First In First Out 선입선출 
*/
public class Main5_Queue {
    public static void main(String[] args) {
        Queue<Integer> que = new LinkedList<>();
   
        // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) -삭제()
        que.offer(5);
        que.offer(2);
        que.offer(3);
        que.offer(7);
        que.poll();
        que.offer(1);
        que.offer(4);
        que.poll();

        while(!que.isEmpty()){
            System.out.print(que.poll() + " ");
        }

        // 출력결과 >> 3 7 1 4
    }
}
