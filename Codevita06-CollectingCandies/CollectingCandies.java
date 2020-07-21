package CodeVitaPrep.DailyPractice.Day2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class CollectingCandies {
    public static int getMinTime(ArrayList<Integer> ci){
        ArrayList<Integer> result = new ArrayList<>();
        while (ci.size()>=2) {
            Collections.sort(ci);
            result.add(ci.get(0) + ci.get(1));
            ci.add(ci.get(0) + ci.get(1));
            ci.remove(0);
            ci.remove(0);
        }
        int sum = 0;
        for(int a:result)
            sum+=a;
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb= new StringBuilder();
        int t = sc.nextInt();
        while (t-->0){
            int size = sc.nextInt();
            ArrayList<Integer> ci =  new ArrayList<>(t);
            for (int i = 0; i < size; i++) {
                ci.add(sc.nextInt());
            }
            sb.append(getMinTime(ci)).append("\n");
        }
        System.out.print(sb);
    }
}

