class Solution {
    public String solution(String my_string) {
        String answer = my_string;
        // String[] arr = {"a", "e", "i", "o", "u"};
        // for (int i=0; i<arr.length; i++) {
        //     answer = answer.replaceAll(arr[i], "");
        // }
        String charsToRemove = "aeiou";
        for (char c : charsToRemove.toCharArray()) {
            answer = answer.replace(String.valueOf(c), "");
        }
        
        return answer;
    }
}