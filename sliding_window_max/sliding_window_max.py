'''
Input: a List of integers as well as an integer `k` 
representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    if len(nums) > 0:
        count = 0
        new_arr = []
        for i in nums:
            if len(nums) - count >= k:
                largest_num = float('-inf')
                for j in nums[count:count+k]:
                    if j > largest_num:
                        largest_num = j
                new_arr.append(largest_num)
                count += 1
        return new_arr






if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
