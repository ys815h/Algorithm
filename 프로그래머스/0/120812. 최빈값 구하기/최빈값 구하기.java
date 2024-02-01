import java.util.*;
class Solution {
    public int solution(int[] array) {
        int answer = 0;
        HashMap<Integer, Integer> hm = new HashMap<>();
        
        for (int i=0; i<array.length; i++) {
            if (hm.containsKey(array[i])) {
                hm.put(array[i], hm.get(array[i])+1);
            } else {
                hm.put(array[i], 1);
            }
        }
        List<Integer> keyList = new ArrayList(hm.keySet());
        List<Integer> valueList = new ArrayList(hm.values());
        
        int max = 0;
        int pre_max = 0;
        int frequency = 0;
        
        for (int i=0; i<valueList.size(); i++) {
            if (max <= valueList.get(i)) {
                pre_max = max;
                max = valueList.get(i);
                frequency = keyList.get(i);
            } 
        }
        if (max == pre_max) {
            answer = -1;
        } else {
            answer = frequency;
        }
        return answer;

    }
}