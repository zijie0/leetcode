package com.zijie;

/**
 * Created by zijie.zy on 2016/4/26.
 */
public class AddDigits {
    public int addDigits(int num) {
        if (num == 0) {
            return 0;
        }
        int mod = num % 9;
        return mod == 0 ? 9 : mod;
    }

    public static void main(String[] args) {
        int[] input = {0, 1, 9, 12, 385, 444, 231};
        for (int i : input) {
            int output = (new AddDigits()).addDigits(i);
            System.out.println(output);
        }
    }
}
