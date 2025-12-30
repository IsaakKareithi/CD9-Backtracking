# Nuts and Bolts problem using Quick Sort

def partition(arr, low, high, pivot):
    """
    Partition function using a pivot from the other array
    """
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] == pivot:
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def match_pairs(nuts, bolts, low, high):
    """
    Matches nuts and bolts using Quick Sort
    """
    if low < high:
        # Choose last bolt as pivot for nuts
        pivot_index = partition(nuts, low, high, bolts[high])

        # Use matched nut as pivot for bolts
        partition(bolts, low, high, nuts[pivot_index])

        # Recursively match left and right subarrays
        match_pairs(nuts, bolts, low, pivot_index - 1)
        match_pairs(nuts, bolts, pivot_index + 1, high)


# Driver code
if __name__ == "__main__":
    nuts = ['@', '#', '$', '%', '^', '&']
    bolts = ['$', '%', '&', '^', '@', '#']

    print("Before matching:")
    print("Nuts: ", nuts)
    print("Bolts:", bolts)

    match_pairs(nuts, bolts, 0, len(nuts) - 1)

    print("\nAfter matching:")
    print("Nuts: ", nuts)
    print("Bolts:", bolts)