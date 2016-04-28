package com.zijie;

/**
 * Created by zijie.zy on 2016/4/28.
 */
public class ClimbStairs {
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        int sum = 0;
        int fib1 = 1;
        int fib2 = 2;
        for (int i = 2; i < n; i++) {
            sum = fib1 + fib2;
            fib1 = fib2;
            fib2 = sum;
        }
        return sum;
    }

    public static void main(String[] args) {
        ClimbStairs climbStairs = new ClimbStairs();
        System.out.println(climbStairs.climbStairs(5));
    }
}
