def binary_search_iterative(sorted_seats, target_seat):
    """
    Iterative Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(1) - Constant auxiliary space
    """
    low = 0
    high = len(sorted_seats) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_seats[mid] == target_seat:
            return mid  # Return the index of the found seat
        elif sorted_seats[mid] < target_seat:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Seat not found


def binary_search_recursive(sorted_seats, target_seat, low, high):
    """
    Recursive Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(log n) - Due to call stack frame accumulation
    """
    if low > high:
        return -1  # Base Case: Seat not found

    mid = (low + high) // 2

    if sorted_seats[mid] == target_seat:
        return mid  # Base Case: Seat found
    elif sorted_seats[mid] < target_seat:
        return binary_search_recursive(sorted_seats, target_seat, mid + 1, high)
    else:
        return binary_search_recursive(sorted_seats, target_seat, low, mid - 1)


# --- Sample Test Execution ---
if __name__ == "__main__":
    # The assignment states the list must be sorted
    train_seats = [10, 14, 21, 25, 30, 42, 55, 68, 77, 89, 93]
    target = 42

    print("Execution Results:")
    print("-" * 30)

    # Testing Iterative Method
    iterative_result = binary_search_iterative(train_seats, target)
    print(f"Iterative Search: Seat {target} found at index {iterative_result}")

    # Testing Recursive Method
    recursive_result = binary_search_recursive(
        train_seats, target, 0, len(train_seats) - 1
    )
    print(f"Recursive Search: Seat {target} found at index {recursive_result}")
