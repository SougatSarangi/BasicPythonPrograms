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
Source Limit: 100 KB'''

''' PROGRAM CODE '''

def primegame(N, RangeInputs):
    for i in range(N):
        num_range = list(RangeInputs[i])
        lower = int(num_range[0])
        upper = int(num_range[-1])    
        prime_num_list = []
        for num in range(lower, upper + 1):            
            if num == 2 or num == 3 or num == 5:
                prime_num_list.append(num)
                pass
            elif num > 2 and num % 2 == 0:
                pass
            else:
                maxDiv = int(num**0.5) + 1                
                for k in range(3, maxDiv):  
                    if (num % k) == 0: 
                        break            
                else:
                    prime_num_list.append(num)
        if len(prime_num_list) == 0:
            print("-1")
        else: 
            print(prime_num_list[-1] - prime_num_list[0])
              
T = int(input())
primeRange = []
for i in range(T):
    num_input = list(input().split())
    primeRange.append(num_input)
primegame(T, primeRange)

