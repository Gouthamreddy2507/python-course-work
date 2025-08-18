
import my_programs as mp

function_map = {
    1: mp.buzz_number,
    2: mp.sum_of_squares,
    3: mp.identity_matrix,
    4: mp.second_smallest,
    5: mp.alternating_case,
    6: mp.even_position_sum,
    7: mp.kaprekar_number,
    8: mp.all_substrings,
    9: mp.mode_list,
    10: mp.merge_sort_lists
}
while True:
    print('''
------ FUNCTION MENU ------
1.Check if a number is a Buzz Number
2.Find sum of squares of first N natural numbers
3.Check if a matrix is identity
4.Find the second smallest element in a list
5.Convert a string to alternating case
6.Find the sum of elements at even positions in a list
7.Check if a number is a Kaprekar Number
8.Generate all substrings of a string
9.Find the mode (most frequent element) in a list
10.Merge and sort two lists
0. Exit
---------------------------''')
    
    choice = int(input("Enter your choice: "))
    if choice > 0 and choice <= len(function_map):
        function_map[choice]()
    elif choice == 0:
        break
    else:
        ("Invalid choice")
