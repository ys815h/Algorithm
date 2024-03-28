import java.util.*;
// 접근방법 1. ArrayList 활용
// class Solution {
//     public int[] solution(String s) {
//         ArrayList<Character> li = new ArrayList<>();
//         int[] answer = new int[s.length()];
//         char temp;
//         for (int i=0; i<s.length(); i++) {
//             temp = s.charAt(i);
//             if (!li.contains(temp)) {
//                 answer[i] = -1;
//             } else {
//                 for (int j=li.size()-1; j>=0; j--) {
//                     if (li.get(j) == temp) {
//                         answer[i] = i - j;
//                         break;
//                     }
//                 }
//             }
//             li.add(i, temp);
//         }
//         return answer;
//     }
// }

// 접근방법 2. Map 활용
class Solution {
    public int[] solution(String s) {
        HashMap<Character, Integer> hm = new HashMap<>();
        int[] answer = new int[s.length()];
        char temp;
        for (int i=0; i<s.length(); i++) {
            temp = s.charAt(i);
            if (!hm.containsKey(temp)) {
                hm.put(temp, i);
                answer[i] = -1;
            } else {
                answer[i] = i - hm.get(temp);
                hm.put(temp, i);
            }
        }
        return answer;
    }
}