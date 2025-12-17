# Structure for an item which stores weight
# and corresponding value of item
class item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# Main greedy function to solve problem
def fractionalKnapsack(w, arr):

    #Sorting item on basis of ratio
    arr.sort(key=lambda x: (x.profit/x.weight), 
             reverse=True)
    
    # Result(value in Knapsack)
    finalvalue = 0.0

    #Looping through all items
    for item in arr:

        # if adding item won't overflow, 
        # add it completely
        if item.weight <= w:
            w -= item.weight
            finalvalue += item.profit

        # if we can't add current item, 
        # add fractional part of it 
        else:
            finalvalue += item.profit * w / item.weight
            break

    # Returning final value
    return finalvalue

# Driver code 
if __name__ == "__main__":
    w = 50
    arr = [item(60, 10), item(100, 20), item(120, 30)]

    #Function call
    max_value = fractionalKnapsack(w, arr)
    print(max_value)