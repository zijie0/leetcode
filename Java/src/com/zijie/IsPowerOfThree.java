package com.zijie;

/**
 * Created by zijie.zy on 2016/4/29.
 */
public class IsPowerOfThree {
    public boolean isPowerOfThree(int n) {
        int Max3PowerInt = 1162261467;
        if (n <= 0 || n > Max3PowerInt) {
            return false;
        }
        return Max3PowerInt % n == 0;
    }
}
