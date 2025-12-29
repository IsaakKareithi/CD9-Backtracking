# max activities
def MaxActivities(arr, n):
    selected = []

    # Sort jobs according to finish time 
    Activity.sort(key=lambda x: x[1])

    # the first activity always gets selected 
    i = 0
    selected.append(arr[i])

    for j in range(1, n):
        '''
        if this activity has start time greater than 
        or equal to the finish time of previously selected
        activity, then select it 
        '''
        if arr[j][0] >= arr[i][1]:
            selected.append(arr[j])
            i = j
        
    return selected

# return driver code
if __name__ == "__main__":
    Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
    n = len(Activity)

    # function call
    selected = MaxActivities(Activity, n)
    print("The following activities are selected: ")
    print(selected[0], end=' ')
    for i in range(0, len(selected)):
        print(",", end=" ")
        print(selected[i], end=' ') 