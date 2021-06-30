words = input().split(" ")
searched_palindrome = input()

palindromes = [p for p in words if p == p[::-1]]
print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")