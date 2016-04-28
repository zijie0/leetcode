package com.zijie;

/**
 * Created by zijie.zy on 2016/4/28.
 */
public class HammingWeight {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ret = 0;
        while(n != 0)
        {
            ret++;
            n -= n & -n;
        }
        return ret;
    }
}
