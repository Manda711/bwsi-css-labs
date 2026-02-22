"""
lab_1c.py

Given a list of numbers, return the maximum sum of any contiguous subarray of the list.

Do not assume anything. Account for all edge cases.

Derived from LeetCode problem: https://leetcode.com/problems/maximum-subarray/ (leetcode medium)
"""
import pytest
# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def max_subarray_sum(nums: list[int]) -> int:
    """
    Function that takes in a list of integers and returns the maximum sum of any contiguous subarray.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: The maximum sum of any contiguous subarray.
    """

    max_current = max_global = nums[0]
    
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
            
    return max_global

# Example usage:
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = max_subarray_sum(nums)
    print(f"Maximum subarray sum: {result}")
def test_standard_case():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_all_positive():
    assert max_subarray_sum([1,2,3,4]) == 10

def test_all_negative():
    assert max_subarray_sum([-5,-2,-8,-1]) == -1

def test_single_element():
    assert max_subarray_sum([7]) == 7

if __name__ == "__main__":
    main()