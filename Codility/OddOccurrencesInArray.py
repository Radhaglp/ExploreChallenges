'''
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
'''
def solution(A):
    # Implement your solution here
    if len(A) < 0:
        return 0
    count_ele = {}
    from collections import Counter
    count_ele = Counter(A)
    for num, freq in count_ele.items():
        if freq % 2 != 0:
            return num

#without inbuilt functions
def solution(A):
    if len(A) < 0:
        return 0
    count_dict = {}
    for num in A:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for key, value in count_dict.items():
        if value % 2 != 0:
            return key
