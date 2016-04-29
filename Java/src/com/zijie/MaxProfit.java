package com.zijie;

/**
 * Created by zijie.zy on 2016/4/29.
 */
public class MaxProfit {
    public int maxProfit(int[] prices) {
        int currentMinPrice = prices.length > 0 ? prices[0] : 0;
        int profit = 0;
        for (int i = 0; i < prices.length; i++) {
            currentMinPrice = Math.min(currentMinPrice, prices[i]);
            profit = Math.max(profit, prices[i] - currentMinPrice);
        }
        return profit;
    }
}
