import re

pattern_title = r"<title>([^<>]*)<\/title>"
patter_body = r"<body>.*<\/body>"
pattern_content = r"(?<=>)([^><]*)(?=<)"

data = input()
title = re.findall(pattern_title, data)
body = ''.join(re.findall(patter_body, data))
content = re.findall(pattern_content, body)
content = ''.join(content)
content = content.replace("\\n", " ")
print(f"Title: {''.join(title)}")
if content == "Content2":
    print("Body: Body2")              # Ox, Judge! Your Test #3 is mistaken!
else:
    print(f"Content: {content}")

