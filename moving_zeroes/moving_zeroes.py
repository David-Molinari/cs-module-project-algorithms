'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    new_arr = []
    if len(arr) > 0:
        for i in arr:
            if len(new_arr) == 0:
                new_arr.append(i)
            else:
                if i == 0:
                    new_arr.append(i)
                else:
                    new_arr.insert(0, i)
        return new_arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")