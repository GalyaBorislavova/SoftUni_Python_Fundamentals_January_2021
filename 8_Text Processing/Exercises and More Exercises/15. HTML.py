title = input()
article_content = input()
comment = input()
list_comments = []

while not comment == "end of comments":
    list_comments.append(comment)
    comment = input()

print(f"<h1>")
print(f"    {title}")
print(f"</h1>")
print(f"<article>")
print(f"    {article_content}")
print(f"</article>")
for c in list_comments:
    print(f"<div>")
    print(f"    {c}")
    print(f"</div>")