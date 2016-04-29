package com.zijie;

import java.util.HashSet;
import java.util.Set;

/**
 * Created by zijie.zy on 2016/4/29.
 */
public class IsHappy {
    private int squareDigitsSum(int n) {
        int sum = 0;
        while (n > 0) {
            int d = n % 10;
            sum += d * d;
            n = n / 10;
        }
        return sum;
    }

    public boolean isHappy(int n) {
        if (n <= 0) {
            return false;
        }
        Set<Integer> s = new HashSet<>();
        s.add(n);
        while (true) {
            n = squareDigitsSum(n);
            if (n == 1) {
                return true;
            }
            if (s.contains(n)) {
                return false;
            }
            s.add(n);
        }
    }
}
