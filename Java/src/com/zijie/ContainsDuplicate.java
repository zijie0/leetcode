package com.zijie;

import java.util.HashSet;
import java.util.Set;

/**
 * Created by zijie.zy on 2016/4/27.
 */
public class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numsSet = new HashSet<>();
        for (int i : nums) {
            numsSet.add(i);
        }
        return nums.length != numsSet.size();
    }
}
