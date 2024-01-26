import java.util.*;
import java.io.*;

class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] arr = my_string.split("");
        
        for (int i=0; i<arr.length; i++) {
            answer += arr[arr.length-i-1];
        }
        
        return answer;
    }
}