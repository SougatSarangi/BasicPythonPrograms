'''
PROBLEM STATEMENT:
    Given an array (or string), the task is to reverse the array/string.

Examples : 
    Input  : arr[] = {1, 2, 3}
    Output : arr[] = {3, 2, 1}

'''

# FUNCTION DEFINATION
def reverseWord(s):
    # Convert string to list
    s = list(s)
    word = []
    
    # A general loop approach   
    # We assign the last element of the loop to the first element
    # second last element to second and so on 
    for i in range(len(s)):
        word.append(s[len(s)-1-i])
    
    # One line Method
    # word = s[::-1]

    # Convert list to string    
    word = ''.join(word)
    return word


# MAIN PROGRAM
if __name__ == "__main__":
    t = int(input("No. of array inputs you want to give: "))
    for i in range(t):
        s = input(f"Array {i+1}")
        print(reverseWord(s))
