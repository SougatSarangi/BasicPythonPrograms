'''
PROBLEM STATEMENT:
    An array contains both positive and negative numbers in random order. 
    Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples  : 
    Input : -12, 11, -13, -5, 6, -7, 5, -3, -6
    Output: -12 -13 -5 -7 -3 -6 11 6 5

Note: Order of elements is not important here.
'''
# FUNCTION DEFINATION
def rearrange(arr):
    ZERO = 0
    neg_array = []
    pos_array = []
    # looping the array to find -ve and +ve values
    # Keep all -ve values in one list and 
    # all +ve values in another list
    # Append both the list
    for i in range(len(arr)):
        if arr[i] < ZERO:
            neg_array.append(arr[i])
        else:
            pos_array.append(arr[i])
    arr = neg_array + pos_array
    
    return arr


# MAIN FUNCTION
if __name__ == "__main__":
    inputList = []
    inputList = [int(item) for item in input("Enter array: ").split()]
    print(rearrange(inputList))