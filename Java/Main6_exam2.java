package Java;

import java.util.*;
import java.lang.*;

/*
  [ 성적이 낮은 순서대로 학생 출력하기 ]
  - N 명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
    각 학생의 이름과 성적 정보가 주어졌을때, 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오. 

  (입력조건)

  (출력조건)

  #입력예시
    2
    홍길동 95
    이순신 77
  #출력예시 
    이순신 홍길동 
*/

class Student implements Comparable<Student>{

    private String name;
    private int score;

    public Student(String name, int score){
        this.name = name;
        this.score = score;
    }

    public String getName() {
        return this.name;
    }

    public int getScore() {
        return this.score;
    }

    // 정렬 기준은 '점수가 낮은 순서'
    @Override
    public int compareTo(Student other) {
        if (this.score < other.score) {
            return -1;
        }
        return 1;
    }
}

public class Main6_exam2 {
    public static void main(String[] args) {
        
        // Scanner sc = new Scanner(System.in);
        // List<Student> array = new ArrayList<>();
        
        // int n = sc.nextInt();
        // sc.nextLine();
       
        // for(int i=0 ; i < n ; i++){
        //     //String name = sc.next();
        //     //int score = sc.nextInt();
        //     String tmp = sc.nextLine();
        //     String[] input = tmp.split(" ");
        //     array.add(new Student(input[0],Integer.parseInt(input[1])));
        // }
        // // 정렬 제대로 안됨.. 
        // Collections.sort(array);
        
        // for(Student obj : array){
        //     System.out.print(obj.getName() + " ");
        // }

        Scanner sc = new Scanner(System.in);

        // N을 입력받기
        int n = sc.nextInt();

        // N명의 학생 정보를 입력받아 리스트에 저장
        List<Student> students = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String name = sc.next();
            int score = sc.nextInt();
            students.add(new Student(name, score));
        }

        Collections.sort(students); // Student 생성자에 에러가 있었네.. 무조건 o ..  

        for (int i = 0; i < students.size(); i++) {
            System.out.print(students.get(i).getName() + " ");
        }

    }
}

