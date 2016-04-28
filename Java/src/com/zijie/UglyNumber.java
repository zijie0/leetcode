package com.zijie;

/**
 * Created by zijie.zy on 2016/4/28.
 */
public class UglyNumber {
    public boolean isUgly(int num) {
        int[] ugly = { 2, 3, 5 };
        if (num < 1) {
            return false;
        }
        for (int x : ugly) {
            while (num % x == 0) {
                num = num / x;
            }
        }
        return num == 1;
    }

    public static void main(String[] args) {
        UglyNumber uglyNumber = new UglyNumber();
        System.out.println(uglyNumber.isUgly(0));
    }
}
