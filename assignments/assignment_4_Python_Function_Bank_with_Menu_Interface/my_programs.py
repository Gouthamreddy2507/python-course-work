
def buzz_number():
    print("Program: Check if a number is a Buzz Number")
    print("""\
def is_buzz(num):
    return num % 10 == 7 or num % 7 == 0
""")
    print("Test Case 1: is_buzz(27) ->", is_buzz(27))  # Ends with 7
    print("Test Case 2: is_buzz(49) ->", is_buzz(49))  # Divisible by 7
    print("Test Case 3: is_buzz(70) ->", is_buzz(70))  # Ends with 0 but divisible by 7
    print("Explanation: A Buzz Number is a number that either ends with digit 7 OR is divisible by 7. "
          "For example, 27 ends with 7, 49 is divisible by 7, and 70 is divisible by 7 even though it doesn't end with 7.")

def is_buzz(num):
    return num % 10 == 7 or num % 7 == 0


def sum_of_squares():
    print("Program: Sum of squares of first N natural numbers")
    print("""\
def sum_squares(n):
    return sum(i*i for i in range(1, n+1))
""")
    print("Test Case 1: sum_squares(3) ->", sum_squares(3))  # 1²+2²+3²=14
    print("Test Case 2: sum_squares(5) ->", sum_squares(5))  # 1²+2²+3²+4²+5²=55
    print("Test Case 3: sum_squares(1) ->", sum_squares(1))  # 1²=1
    print("Explanation: Uses a generator expression to square each number from 1 to N and sum them all. "
          "The result is the total of squares, e.g., for N=3 → 1+4+9 = 14.")

def sum_squares(n):
    return sum(i*i for i in range(1, n+1))


def identity_matrix():
    print("Program: Check if a matrix is Identity")
    print("""\
def is_identity(mat):
    size = len(mat)
    return all(mat[i][j] == (1 if i == j else 0) for i in range(size) for j in range(size))
""")
    print("Test Case 1: is_identity([[1,0],[0,1]]) ->", is_identity([[1,0],[0,1]]))
    print("Test Case 2: is_identity([[1,0],[1,0]]) ->", is_identity([[1,0],[1,0]]))
    print("Test Case 3: is_identity([[1,0,0],[0,1,0],[0,0,1]]) ->", is_identity([[1,0,0],[0,1,0],[0,0,1]]))
    print("Explanation: An identity matrix has 1s on its main diagonal and 0s elsewhere. "
          "The function checks every element's position and ensures the rule is satisfied.")

def is_identity(mat):
    size = len(mat)
    return all(mat[i][j] == (1 if i == j else 0) for i in range(size) for j in range(size))


def second_smallest():
    print("Program: Find second smallest element in a list")
    print("""\
def second_smallest_element(lst):
    return sorted(set(lst))[1]
""")
    print("Test Case 1: second_smallest_element([4,1,7,1]) ->", second_smallest_element([4,1,7,1]))
    print("Test Case 2: second_smallest_element([10,20,5,15]) ->", second_smallest_element([10,20,5,15]))
    print("Test Case 3: second_smallest_element([3,3,3,5]) ->", second_smallest_element([3,3,3,5]))
    print("Explanation: Removes duplicates using a set, sorts the numbers, and returns the second smallest value. "
          "This avoids counting repeated numbers as separate.")

def second_smallest_element(lst):
    return sorted(set(lst))[1]


def alternating_case():
    print("Program: Convert a string to alternating case")
    print("""\
def alt_case(s):
    return ''.join(c.lower() if i % 2 else c.upper() for i, c in enumerate(s))
""")
    print("Test Case 1: alt_case('hello') ->", alt_case("hello"))
    print("Test Case 2: alt_case('python') ->", alt_case("python"))
    print("Test Case 3: alt_case('Alternate') ->", alt_case("Alternate"))
    print("Explanation: Iterates through the string and changes characters at even indexes to uppercase "
          "and at odd indexes to lowercase, giving an alternating pattern.")

def alt_case(s):
    return ''.join(c.lower() if i % 2 else c.upper() for i, c in enumerate(s))


def even_position_sum():
    print("Program: Sum of elements at even positions in a list")
    print("""\
def sum_even_positions(lst):
    return sum(lst[i] for i in range(0, len(lst), 2))
""")
    print("Test Case 1: sum_even_positions([1,2,3,4]) ->", sum_even_positions([1,2,3,4]))
    print("Test Case 2: sum_even_positions([10,5,20,5]) ->", sum_even_positions([10,5,20,5]))
    print("Test Case 3: sum_even_positions([0,1,0,1,0]) ->", sum_even_positions([0,1,0,1,0]))
    print("Explanation: Adds up all numbers located at even index positions (0, 2, 4, ...). "
          "Note: Index 0 is considered even.")

def sum_even_positions(lst):
    return sum(lst[i] for i in range(0, len(lst), 2))


def kaprekar_number():
    print("Program: Check if a number is a Kaprekar Number")
    print("""\
def is_kaprekar(n):
    sq = str(n**2)
    right = sq[-len(str(n)):] if len(sq) > 1 else sq
    left = sq[:-len(str(n))] if sq[:-len(str(n))] else "0"
    return n == int(left) + int(right)
""")
    print("Test Case 1: is_kaprekar(45) ->", is_kaprekar(45))
    print("Test Case 2: is_kaprekar(9) ->", is_kaprekar(9))
    print("Test Case 3: is_kaprekar(10) ->", is_kaprekar(10))
    print("Explanation: Square the number, split it into two parts (rightmost digits equal in length to the original number), "
          "and sum them. If the sum equals the original number, it’s a Kaprekar number.")

def is_kaprekar(n):
    sq = str(n**2)
    right = sq[-len(str(n)):] if len(sq) > 1 else sq
    left = sq[:-len(str(n))] if sq[:-len(str(n))] else "0"
    return n == int(left) + int(right)


def all_substrings():
    print("Program: Generate all substrings of a string")
    print("""\
def substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
""")
    print("Test Case 1: substrings('abc') ->", substrings("abc"))
    print("Test Case 2: substrings('ab') ->", substrings("ab"))
    print("Test Case 3: substrings('xy') ->", substrings("xy"))
    print("Explanation: Uses two nested loops to slice the string at every possible start and end position. "
          "Generates all continuous substrings.")

def substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]


def mode_list():
    print("Program: Find mode (most frequent element) in a list")
    print("""\
from collections import Counter
def find_mode(lst):
    counts = Counter(lst)
    return max(counts, key=counts.get)
""")
    print("Test Case 1: find_mode([1,2,2,3]) ->", find_mode([1,2,2,3]))
    print("Test Case 2: find_mode(['a','b','a']) ->", find_mode(['a','b','a']))
    print("Test Case 3: find_mode([5,5,1,1,1]) ->", find_mode([5,5,1,1,1]))
    print("Explanation: Uses Counter to count frequency of each element, then returns the element with the maximum count. "
          "If multiple values have the same frequency, returns the first max found.")

from collections import Counter
def find_mode(lst):
    counts = Counter(lst)
    return max(counts, key=counts.get)


def merge_sort_lists():
    print("Program: Merge and sort two lists")
    print("""\
def merge_and_sort(l1, l2):
    return sorted(l1 + l2)
""")
    print("Test Case 1: merge_and_sort([3,1],[2,4]) ->", merge_and_sort([3,1],[2,4]))
    print("Test Case 2: merge_and_sort([10,5],[5,10]) ->", merge_and_sort([10,5],[5,10]))
    print("Test Case 3: merge_and_sort([], [1,2]) ->", merge_and_sort([], [1,2]))
    print("Explanation: Combines both lists using + operator, then sorts them into ascending order. "
          "Works for numbers, strings, and any sortable elements.")

def merge_and_sort(l1, l2):
    return sorted(l1 + l2)
