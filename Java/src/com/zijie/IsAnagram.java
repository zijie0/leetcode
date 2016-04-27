package com.zijie;

import java.util.Arrays;

/**
 * Created by zijie.zy on 2016/4/27.
 */
public class IsAnagram {
    public boolean isAnagram(String s, String t) {
        if (s == null && t == null) {
            return true;
        }
        if (s == null || t == null) {
            return false;
        }
        if(s.length() != t.length()) {
            return false;
        }
        char[] S= s.toCharArray();
        char[] T= t.toCharArray();
        Arrays.sort(S);
        Arrays.sort(T);

        return Arrays.equals(S, T);
    }
}
