def linear_search(A, target):
    for i, num in enumerate(A):
        if num == target:
            return i
    return -1


def binary_search(A, target):
    first = 0
    last = len(A) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if A[mid] == target:
            index = mid
        else:
            if target < A[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


def interpolation_search(A, target):
    left, right = 0, len(A) - 1
    while left <= right and A[left] <= target <= A[right]:
        if left == right:
            if A[left] == target:
                return left
            return -1

        estimated_pos = left + ((target - A[left]) * (right - left)) // (A[right] - A[left])

        if A[estimated_pos] == target:
            return estimated_pos
        elif A[estimated_pos] < target:
            left = estimated_pos + 1
        else:
            right = estimated_pos - 1
    return -1
