import java.util.*;

public class Solution {
    public ArrayList<Integer> solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        int temp = -1;
        for (int i=0; i<arr.length; i++) {
            if (temp != arr[i]) {
                answer.add(arr[i]);
            }
            temp = arr[i];
        }
        return answer;
    }
}