package com.zijie;

/**
 * Created by zijie.zy on 2016/4/26.
 */
public class ReverseString {
    public String reverseString(String s) {
        StringBuilder ans = new StringBuilder(s);
        return ans.reverse().toString();
    }

    public static void main(String[] args) {
        String input = "Hello";
        String output = (new ReverseString()).reverseString(input);
        System.out.println(output);
    }
}
