package com.zijie;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by zijie.zy on 2016/4/29.
 */
public class ReverseVowels {
    public String reverseVowels(String s) {
        if (s == null || s.length() <= 1) {
            return s;
        }
        char[] chs = s.toCharArray();
        Set<Character> vowels = new HashSet<>(Arrays.asList(
                'a', 'e', 'i', 'o', 'u',
                'A', 'E', 'I', 'O', 'U'
        ));
        int low = 0;
        int high = chs.length - 1;
        while (low < high) {
            while (low < high && !vowels.contains(chs[low])) {
                low++;
            }
            while (low < high && !vowels.contains(chs[high])) {
                high--;
            }
            if (low != high) {
                char tmp = chs[low];
                chs[low] = chs[high];
                chs[high] = tmp;
                low++;
                high--;
            } else {
                break;
            }
        }
        return new String(chs);
    }

    public static void main(String[] args) {
        ReverseVowels reverseVowels = new ReverseVowels();
        String res = reverseVowels.reverseVowels("Hello");
        System.out.println(res);
    }
}
