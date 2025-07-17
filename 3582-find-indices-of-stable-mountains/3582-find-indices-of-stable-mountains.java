
import java.util.*;
class Solution {
    public List<Integer> stableMountains(int[] heights, int threshold) {
        List<Integer> stableIndices = new ArrayList<>();
        
        for (int i = 1; i < heights.length; i++) {
            if (heights[i-1] > threshold) {
                stableIndices.add(i);
            }
        }
        return stableIndices;
    }
}