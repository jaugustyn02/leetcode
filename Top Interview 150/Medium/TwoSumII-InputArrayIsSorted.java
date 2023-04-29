/*
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
*/

// Time complexity: O(n)
// Space complexity: O(1)


class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int sol[] = new int[2];
        int i = 0, j = numbers.length-1;
        while(true){
            int curr_sum = numbers[i] + numbers[j];
            if (curr_sum == target) break;
            else if (curr_sum < target) ++i;
            else --j;
        }
        sol[0] = i+1;
        sol[1] = j+1;
        return sol;
    }
}
