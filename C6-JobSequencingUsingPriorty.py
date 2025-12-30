#python program for the above aproach

import heapq

def printJobScheduling(arr):
    n = len(arr)

    # arr[i][o] = job_id, arr[i][1] = deadline, arr[i][2] = profit 

    # sorting the array on the  
    # basis of their deadlines
    arr.sort(key=lambda x: x[1])

    # Initialize the result array and maxHeap
    result = []
    maxHeap = []

    # Starting the iteration from the end
    for i in range(n -1, -1, -1):

        # Calculate the slots between two deadlines
        if i == 0:
            slot_available = arr[i][1]
        else:
            slot_available = arr[i][1] - arr[i-1][1]

    # Include the profit of job(as priority) 
    # deadline and job_id in maxHeap
    # NOte: we push negative value in maxHeap
    # to convert minHeap to maxHeap in python

        heapq.heappush(maxHeap, (-arr[i][2], arr[i][1], arr[i][0]))     

    while slot_available and maxHeap:       

        # Get the job with max profits 
        profit, deadline, job_id = heapq.heappop(maxHeap)

        # reduce the slots 
        slot_available -= 1

        # Incluse job in the result array
        result.append([job_id, deadline])

    # Jobs included might be shuffled
    # Sort reslut array by their dealines
    result.sort(key=lambda x: x[1])

    for job in result:
        print(job[0], end=' ')
    print()

# Driver code
if __name__ == "__main__":
    arr = [['a', 2, 100],
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]
    
    print("The following is the maximum sequence of jobs: ")

    # Functoin call
    printJobScheduling(arr)