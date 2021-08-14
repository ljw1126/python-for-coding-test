package Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main5_BFS {

    public static boolean[] visited = new boolean[9];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
    //public static Queue<Integer> queue = new LinkedList();

    public static void main(String[] args) {
        
        for(int i=0;i<9;i++){
            graph.add(new ArrayList<Integer>());
        }
        // 노드 1 
        graph.get(1).add(2);
        graph.get(1).add(3);
        graph.get(1).add(8);
       
        // 노드 2        
        graph.get(2).add(1);
        graph.get(2).add(7);
       
        // 노드 3
        graph.get(3).add(1);
        graph.get(3).add(4);
        graph.get(3).add(5);
       
        // 노드 4
        graph.get(4).add(3);
        graph.get(4).add(5);
       
        // 노드 5
        graph.get(5).add(3);
        graph.get(5).add(4);
       
        // 노드 6
        graph.get(6).add(7);
       
        // 노드 7
        graph.get(7).add(2);
        graph.get(7).add(6);
        graph.get(7).add(8);
        // 노드 
        graph.get(8).add(1);
        graph.get(8).add(7);

        //bfs(1);    
        test(1);
    }

    public static void bfs(int start){
        // 교재 해설 
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);  // start 노드 넣음 
        
        //현재 노드 방문 처리 
        visited[start] = true; 
       
        // 큐가 빌때까지 반복 
        while (!q.isEmpty()){
            int x = q.poll();
            System.out.print(x + " ");
            // 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입 
            for(int i=0; i < graph.get(x).size() ; i++){
                int node = graph.get(x).get(i);
                if(!visited[node]) {
                    q.offer(node);
                    visited[node] = true; // 여기가 틀렸네 .. 넣는건 전부 true처리, 중복 안들어가짐 
                }
            }

            //System.out.println("q >> "+  q);
            //System.out.println("visited >>" + Arrays.toString(visited));
        }

        /*
        //내소스 (틀림) >> 1 2 3 8 7 4 5 ^7 6 5 6$ 
        if (x == 1) queue.addAll(graph.get(x));
        
        visited[x] = true; 
        
        System.out.print(x + " ");
       
        while ( !queue.isEmpty() ){
            
            int next = queue.poll();  
            
             for(int i=0; i < graph.get(next).size() ; i++){
                 int node = graph.get(next).get(i);
                 if(!visited[node]) queue.offer(node);
             }
         
             bfs(next);
        
        }
        */
    }

    public static void test(int start){
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        visited[start] = true;
        System.out.println("결과====");
        while(!q.isEmpty()){

            int x = q.poll();
            System.out.print(x + " ");

            for(int i =0; i < graph.get(x).size(); i++){
                int y = graph.get(x).get(i);
                if(!visited[y]){
                    q.offer(y);
                    visited[y] = true;
                }
            }
        }
    }

}
