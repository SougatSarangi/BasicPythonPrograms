'''
PROBLEM STATEMENT:
    Find min and max value of an array

Example:
    Input: 1, 3, 5, -4, 10, -29
    Output: Max Value: 10
            Min Value: -29
'''
# FUNCTION DEFINATION
def minmax(arr):
    # if array has 1 element, then min and max are same value
    if len(arr) == 1:
        min_value = arr[0]
        max_value = arr[0]

    # if array has more than 1 element    
    else:
        # Initialization
        min_value = arr[0]
        max_value = arr[1]
        
        # looping the array to find min and max values
        for i in range(len(arr)):
            if arr[i] > max_value:
                max_value = arr[i]
                
            elif arr[i] < min_value:
                min_value = arr[i]
                
    print("Max Value: ", max_value)
    print("Min Value: ", min_value)

    # DIRECT METHODS TO FIND THE SOLUTION                    
    #min_value = min(arr)
    #max_value = max(arr)

    # return min_value, max_value


# MAIN PROGRAM
inputList = []
inputList = [int(item) for item in input("Enter the array: ").split()]
print(minmax(inputList))