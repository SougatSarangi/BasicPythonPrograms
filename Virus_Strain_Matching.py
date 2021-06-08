''' PROBLEM STATEMENT'''
''' 
Virus Outbreak (100 Marks)
------------------------------------------------------------------------------------------------------------------ 
In the Martian land faraway, a new virus has evolved and is attacking the individuals at a fast pace. 
The scientists have figured out the virus composition, V. The big task is to identify the people who 
are infected. The sample of N people is taken to check if they are POSITIVE or NEGATIVE. A report is 
generated which provides the current blood composition B of the person. 
------------------------------------------------------------------------------------------------------------------ 
POSITIVE or NEGATIVE ?

If the blood composition of the person is a subsequence of the virus composition V, then the person is
identified as POSITIVE otherwise NEGATIVE.
------------------------------------------------------------------------------------------------------------------ 
Example:
------------------------------------------------------------------------------------------------------------------ 
Virus Composition, V = coronavirus
Blood Composition of the person , B = ravus
The person in question is POSITIVE as B is the subsequence of the V.
 
The scientists are busy with their research for medicine and request you to build a program which can 
quickly figure out if the person is POSITIVE or NEGATIVE. They will provide you with the virus 
composition V and all the people’s current blood composition. Can you help them?
------------------------------------------------------------------------------------------------------------------ 
Note: The virus and blood compositions are lowercase alphabet strings.
------------------------------------------------------------------------------------------------------------------ 
Input Format:
- The first line of the input consists of the virus composition, V
- The second line of he input consists of the number of people, N
- Next N lines each consist of the blood composition of the ith person, Bi
------------------------------------------------------------------------------------------------------------------ 
Constraints:
- 1<= N <=10
- 1<= |B|<= |V|<= 10^5
------------------------------------------------------------------------------------------------------------------ 
Output Format:
- For each person, print POSITIVE or NEGATIVE in a separate line
------------------------------------------------------------------------------------------------------------------ 
Sample TestCase 1
Input:
    coronavirus <-- Virus Strain to be searched
    3           <-- No. of patients
    abcde       <-- Blood Composition of patient[0]
    crnas       <-- Blood Composition of patient[1]
    onarous     <-- Blood Composition of patient[2]

Output:
    NEGATIVE
    POSITIVE
    NEGATIVE
------------------------------------------------------------------------------------------------------------------ 
Time Limit(X): 0.50 sec(s) for each input.
Memory Limit: 512 MB
Source Limit: 100 KB 
------------------------------------------------------------------------------------------------------------------ 
------------------------------------------------------------------------------------------------------------------ 
------------------------------------------------------------------------------------------------------------------ '''


''' ------------------------------ PROGRAM CODE ------------------------------ '''

# Function for finding the test result

def testresult(Virus, N, NameList):

    # Convert the Virus string into a list with letters of the string as elements
    # EXAMPLE:  Virus = CORONA     then     V = ['C' 'O' 'R' 'O' 'N' 'A']
    V = list(Virus)
    
    for i in range(len(NameList)):
        
        # Innitialize count variable which counts the number of elements in NameList
        # that matched with the elements of virus list V
        count = 0
        
        # Convert elements of NameList to a list containing letters of the elements
        # EXAMPLE:  NameList[0] = ABCDE     then  inputList = ['A' 'B' 'C' 'D' 'E']
        inputList = list(NameList[i])
        
        # WHILE loop counter
        k = 0
        
        # Check the inputList and compare each element with elements of V (virus strain list)
        for j in range(len(inputList)):
            while k < len(V):
            
                # if element of inputList doesn't match element of V, 
                # then move on and check next element
                if inputList[j] != V[k]:
                    pass
                else:
                # when it matches, then increment the count
                    count += 1
                    break
                
                # Increment the while loop counter
                k += 1
                    
        # Reset the inputList to a blank list for the next input from the for loop
        inputList = []        

        # Compare the count with length of the element in NameList
        # If the count matches then it's POSITIVE else it's NEGATIVE
        if count == len(NameList[i]):
            print("POSITIVE")
        else:
            print("NEGATIVE")


''' ------------------- MAIN FUNCTION TO TAKE INPUTS -----------------------------------''' 
# Take input of the Virus Strain to be checked
V = input()

# Define number of patient strains to be taken by the compiler
N = int(input())

# Take input of the patient strains in a list
ele = 0
B = []
for ele in range (N):
    patient = list(input())
    B.append(patient)

# Call the testresult function to get the results
testresult(V, N, B)