import re

pattern = r"\d+"
text = input()
nums = []
while text:
    nums.extend(re.findall(pattern, text))
    text = input()
print(*nums)