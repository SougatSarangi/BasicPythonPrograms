''' PROBLEM STATEMENT'''
'''
Prime Game (100 Marks)
Rax, a school student, was bored at home in the pandemic. He wanted to play but there was no one to play with. 
He was doing some mathematics questions including prime numbers and thought of creating a game using the same. 
After a few days of work, he was ready with his game. He wants to play the game with you.

------------------------------------------------------------------------------------------------------------------
GAME:
------------------------------------------------------------------------------------------------------------------
Rax will randomly provide you a range [ L , R ] (both inclusive) and you have to tell him the maximum difference
between the prime numbers in the given range. There are three answers possible for the given range.
    1. There are two distinct prime numbers in the given range so the maximum difference can be found.
    2. There is only one distinct prime number in the given range. The maximum difference in this case would be 0.
    3. There are no prime numbers in the given range. The output for this case would be -1.
To win the game, the participant should answer the prime difference correctly for the given range.

------------------------------------------------------------------------------------------------------------------
Example:
------------------------------------------------------------------------------------------------------------------
Range: [ 1, 10 ]
The maximum difference between the prime numbers in the given range is 5.
Difference = 7 - 2 = 5

Range: [ 5, 5 ]
There is only one distinct prime number so the maximum difference would be 0.

Range: [ 8 , 10 ]
There is no prime number in the given range so the output for the given range would be -1.

Can you win the game?
------------------------------------------------------------------------------------------------------------------
Input Format:
    The first line of input consists of the number of test cases, T
    Next T lines each consists of two space-separated integers, L and R
------------------------------------------------------------------------------------------------------------------
Constraints:
    1<= T <=10
    2<= L<= R<=10^6
------------------------------------------------------------------------------------------------------------------
Output Format:
    For each test case, print the maximum difference in the given range in a separate line. 
------------------------------------------------------------------------------------------------------------------
Sample TestCase 1
Input:
    5
    5 5
    2 7
    8 10
    10 20
    4 5
    
Output:
    0
    5
    -1
    8
    0
------------------------------------------------------------------------------------------------------------------    
Explanation:
    Test Case 1: [ 5 - 5 ] = 0
    Test Case 2: [ 7 - 2 ] = 5
    Test Case 3: No prime number in the given range. Output = -1
    Test Case 4: [ 19 - 11 ] = 8
    Test Case 5: The difference would be 0 since there is only one prime number in the given range.
------------------------------------------------------------------------------------------------------------------
Time Limit(X): 0.50 sec(s) for each input.
Memory Limit: 512 MB
Source Limit: 100 KB
------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------'''

''' PROGRAM CODE '''
'''
# Function to find Prime Numbers                        # ^
def primenumbers(lowerbound, upperbound):               # |
    prime_num = []                                      # |
                                                        # |
    for num in range(lowerbound, upperbound + 1):       # |     
        if num == 2 or num == 3 or num == 5:            # |
            prime_num.append(num)                       # |
            pass                                        # |
        elif num > 2 and num % 2 == 0:                  # |  <--- An alternate method to find primes
            pass                                        # |  <--- But with higher time complexity   
        else:                                           # |
            maxDiv = int(num**0.5) + 1                  # |
            for k in range(3, maxDiv):                  # |
                if (num % k) == 0:                      # |
                    break                               # |    
            else:                                       # |
                prime_num.append(num)                   # |            
    return prime_num                                    # V
'''  
 
''' while the above code serves the purpose but it has a higher time complexity
    Hence it needs to be optimized.
    A better alternative is given below - also called SEIVE METHOD of finding primes
'''           

'''    
    In Seive Method we will run the loop till sqrt(upperbound)
    Because any multiple after that is the reverse of what was there before that
    EXAMPLE:
        Multiples of 36:
        1 x 36      A
        2 x 18      |   We will only consider this to check
        3 x 12      |
        4 x 9       V
      -------------  
        6 x 6       <------ sqrt(36) = 6
      -------------  
        9 x 4
        12 x 3
        18 x 2
        36 x 1
'''

# SEIVE METHOD to find Prime Numbers

def seiveprimenumbers(lowerbound, upperbound):
    # Define an empty list to store the prime numbers
    prime_num = []
    
    # SET all the values in the range [2, upperbound + 1] as TRUE
    prime = [True for i in range(upperbound + 1)]
    
    # Innitialize a variable p
    p = 2
    
    # Check the loop till p^2 <= upperbound.
    # Why? -> Description given above the function defination
    while (p*p <= upperbound):
        if (prime[p] == True):
        
            # Check other multiples of the number p and if found set it as False
            for j in range(p*p, upperbound + 1, p):
                prime[j] = False
        
        # increment p to run the while loop
        p += 1
    
    # Now loop through the list and check which elements are True
    for p in range(lowerbound, upperbound + 1):
        # If found true then append it to the prime_num list
        if prime[p]:
            prime_num.append(p)
    
    return prime_num
                
 
# Function to play the game
def primegame(N, RangeInputs):
    for i in range(N):
        # Take each element of RangeInputs as list
        num_range = list(RangeInputs[i])
        
        # Define the lower bound and upper bound from the input list
        lower = int(num_range[0])
        upper = int(num_range[-1]) 

        # Call the primenumbers function to find a list of prime numbers
        prime_num_list = seiveprimenumbers(lower, upper)
        
        if len(prime_num_list) == 0:
            # Condition for no prime numbers
            print("-1")
        
        else: 
            # difference between max and min values of prime numbers found in list
            print(prime_num_list[-1] - prime_num_list[0])

''' ------------------- MAIN FUNCTION TO TAKE INPUTS -----------------------------------'''              
# Define number of range inputs to be taken by the compiler
T = int(input())

# Innitialize list to take the range inputs and keep it in a list 
# primeRange = [ [l1 r1], [l2 r2], [l3 r3], .... ]
primeRange = []
for i in range(T):
    # take input as list item and split them at space b/w them
    num_input = list(input().split())
    primeRange.append(num_input)
    
# Call the primegame function    
primegame(T, primeRange)

