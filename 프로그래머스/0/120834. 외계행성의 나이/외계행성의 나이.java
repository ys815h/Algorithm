import java.util.*;
class Solution {
    public String solution(int age) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        List<Integer> li = new ArrayList<>();
        
        while(age > 0) {
            if (age == 0) {
                li.add(age);
            }
            li.add(age%10);
            age /= 10;
        }
        
        for (int i=li.size()-1; i>=0; i--) {
            sb.append((char)(li.get(i)+97));
        }
        
        answer = String.valueOf(sb);
        return answer;
    }
}