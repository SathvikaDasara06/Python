def sum_of_squares_of_even(nums: list) -> int:
    '''Return the sum of squares of all even numbers in the list.

    Args:
        nums : list - list of integers

    Returns:
        int - sum of squares of all even numbers
    '''
    
    return sum(x**2 for x in nums if x % 2 == 0)
at=sum_of_squares_of_even([1,2,3,4,5,6])
print(at)
