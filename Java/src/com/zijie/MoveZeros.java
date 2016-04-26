package com.zijie;

/**
 * Created by zijie.zy on 2016/4/26.
 */
public class MoveZeros {
    public void moveZeroes(int[] nums) {
        int shift = 0;
        int size = nums.length;
        for (int i = 0 ; i < size; i++) {
            if (nums[i] == 0) {
                shift++;
            } else {
                nums[i - shift] = nums[i];
            }
        }
        for (int i = size - shift; i < size; i++) {
            nums[i] = 0;
        }
    }

    public static void main(String[] args) {
        MoveZeros moveZeros = new MoveZeros();
        int[] nums = {1, 0, 0, 0, 2, 3, 0};
        moveZeros.moveZeroes(nums);
        for (int i : nums) {
            System.out.print(String.valueOf(i) + " ");
        }
    }
}
