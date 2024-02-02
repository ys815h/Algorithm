import java.util.*;
class Solution {
    public String solution(String letter) {
        String answer = "";
        String[] morseList = {".-","-...","-.-.","-..",".","..-.",
    "--.","....","..",".---","-.-",".-..",
    "--","-.","---",".--.","--.-",".-.",
    "...","-","..-","...-",".--","-..-",
    "-.--","--.."};
        
        String[] arr = letter.split(" ");
        for (String val : arr) {
            answer += (char) (Arrays.asList(morseList).indexOf(val) + 97);
        }
        return answer;
    }
}