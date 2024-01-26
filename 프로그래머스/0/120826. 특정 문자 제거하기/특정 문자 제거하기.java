import java.util.*;
class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        
        if (my_string != null) {
            answer = my_string.replace(letter, "");
        }
        
        return answer;
    }
}