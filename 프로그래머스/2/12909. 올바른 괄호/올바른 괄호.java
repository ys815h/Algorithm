import java.util.*;
class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        char[] arr = s.toCharArray();
        
        for(char val : arr) {
            if (!stack.isEmpty()) {
                if(stack.peek() == '(' && val == ')') {
                    stack.pop();
                    continue;
                }
            }
            stack.push(val);
        }
        return stack.isEmpty();
    }
}