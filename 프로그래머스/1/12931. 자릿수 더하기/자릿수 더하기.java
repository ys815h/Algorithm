import java.util.*;
import java.io.*;
public class Solution {
    public int solution(int n) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int answer = 0;
        String N = Integer.toString(n);
        String[] arr = N.split("");
        
        for (int i=0; i < arr.length; i++) {
            answer += Integer.parseInt(arr[i]);
        }
        bw.flush();
        
        
        return answer;
    }
}