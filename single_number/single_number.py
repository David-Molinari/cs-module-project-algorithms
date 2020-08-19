'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    if len(arr) > 0:
        arr.sort()
        count = 0
        for i in arr:
            if count == 0:
                if i != arr[count+1]:
                    return i
                else:
                    count += 1
            elif count == len(arr)-1:
                if i != arr[count-1]:
                    return i
                else:
                    return None
            elif i != arr[count+1] and i != arr[count-1]:
                return i
            else:
                count += 1

            

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")