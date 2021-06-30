def palindrome(number_list: list):
    for num in numbers:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
palindrome(numbers)

# positive_numbers = input().split(", ")
#
#
# def palindrome(list_numbers: Lists and Functions):
#     right = []
#     left = []
#     is_palindrome = False
#     for num in range(len(list_numbers)):
#         current_num = list_numbers[num]
#         for digits in range(len(current_num)):
#             right.append(current_num[digits])
#         for digit in range(len(current_num) - 1, -1, -1):
#             left.append(current_num[digit])
#         for i in range(len(right)):
#             if left[i] == right[i]:
#                 is_palindrome = True
#                 continue
#             else:
#                 is_palindrome = False
#                 break
#         right = []
#         left = []
#         if is_palindrome:
#             result = True
#         else:
#             result = False
#         print(result)
#
#
# palindrome(positive_numbers)

