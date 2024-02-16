import java.util.*;
class Solution {
    public int solution(int[] nums) {
        List<Integer> li = new ArrayList<>();
        for (int i=0; i<nums.length; i++) {
            if (li.size() == nums.length/2) break;
            if(li.contains(nums[i])) {
                continue;
            } else {
                li.add(nums[i]);
            }
        }
        int answer = li.size();
        return answer;
    }
}