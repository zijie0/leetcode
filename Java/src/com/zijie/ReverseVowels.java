package com.zijie;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by zijie.zy on 2016/4/29.
 */
public class ReverseVowels {
    public String reverseVowels(String s) {
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        for (char c : s.toCharArray()) {
            if (vowels.contains(c)) {
                System.out.println(c);
            }
        }
        return null;
    }

    public static void main(String[] args) {
        ReverseVowels reverseVowels = new ReverseVowels();
        reverseVowels.reverseVowels("Hello");
    }
}
