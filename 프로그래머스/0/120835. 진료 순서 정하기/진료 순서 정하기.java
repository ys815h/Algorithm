import java.util.*;
class Solution {
    public int[] solution(int[] emergency) {
        int[] arr = Arrays.copyOf(emergency, emergency.length);
        Arrays.sort(arr);
        
        int[] answer = new int[emergency.length];
        for (int i=0; i<emergency.length; i++) {
            for(int j=arr.length-1; j>=0; j--) {
                if(emergency[i] == arr[j]) {
                    answer[i] = arr.length-j;
                }
            }
        }
        
        return answer;
    }
}
