'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, DP = None):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    # Your code here
    if DP == None:
        DP = [0 for i in range(0, n + 1)] 
      
    # base cases 
    DP[0] = DP[1] = 1
    DP[2] = 2
  
    # Iterate for all values from 4 to n 
    for i in range(3, n + 1): 
        DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3] 
      
    return DP[n] 
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
