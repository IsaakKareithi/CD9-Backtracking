def printJobScheduling(arr, t):

    # Length of array
    n = len(arr)

    #Sort all jobs according to 
    # decreasing order of profits
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    # To keep track of tree time slots
    result = [False] * t

    # To store results (sequence of jobs)
    job = ['-1'] * t

    # Iterate through all given jobs
    for i in range(len(arr)):

        # Find a free slot for this job
        # Note: Start from the last possible slot
        for j in range(min(t - 1, arr[i][1] -1 ), -1, -1):

            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
    
    # print the sequence
    print(job)

# Driver code
if __name__ == '__main__':
    arr = [['a', 2, 100],
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]

    print("The following is the maximum profit sequence of jobs: ")

    #Function call
    printJobScheduling(arr, 3)