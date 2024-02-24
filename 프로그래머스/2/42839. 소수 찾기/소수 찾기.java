// 고려할 점 1. 배열의 길이가 1~numbers.length()까지의 arr배열을 넘겨줘야한다

import java.util.*;

class Solution {
    static ArrayList<Integer> arr = new ArrayList<>();;
    static boolean[] visited;
    
    public int solution(String numbers) {
        int answer = 0;
        visited = new boolean[numbers.length()];
        
        for (int i=0; i<numbers.length(); i++) {
            DFS(numbers, "", i+1);
        }
        
        for (int i=0; i<arr.size(); i++) {
            // System.out.println("arr(" + i + ") 값 " + arr.get(i));
            if (Prime(arr.get(i))) answer++;
        }
        return answer;
    }
        
   static void DFS(String str, String temp, int m) {
        if (temp.length() == m) {
            int num = Integer.parseInt(temp);
            if (!arr.contains(num) && num > 1) arr.add(num);
            return;
        }
        
        for (int i=0; i<str.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                temp += str.charAt(i);
                DFS(str, temp, m);
                temp = temp.substring(0, temp.length()-1);
                visited[i] = false;
            }
        }
        return;
    }
    static boolean Prime(int a) {
        int p = 0;
        for (int i=1; i<=(int) Math.sqrt(a); i++) {
            if (a % i == 0) p += 1;
            if (p > 1) break;
        }
        return p == 1 ? true : false;
    }
}