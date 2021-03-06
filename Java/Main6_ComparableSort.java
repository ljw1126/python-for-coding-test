package Java;

import java.util.*;
// Comparable 인터페이스 .. 이해 덜됨 .. 
public class Main6_ComparableSort {
    public static void main(String[] args) {
        List<Fruit> fruits = new ArrayList<>();

        fruits.add(new Fruit("바나나", 2));
        fruits.add(new Fruit("사과", 5));
        fruits.add(new Fruit("당근", 3));

        Collections.sort(fruits);
        
        for(Fruit fruit : fruits){
            System.out.printf("(%s,%d)\n",fruit.getName(),fruit.getScore());
        }
    }
}

class Fruit implements Comparable<Fruit>{
    private String name;
    private int score;

    public Fruit(String name, int score){
        this.name = name;
        this.score = score;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getScore() {
        return this.score;
    }

    public void setScore(int score) {
        this.score = score;
    }
    // 정렬 기준은 '점수가 낮은 순서'
    @Override
    public int compareTo(Fruit o) {
        if(getScore() < o.score) {
            return -1;
        }
        return 1;
    }

}