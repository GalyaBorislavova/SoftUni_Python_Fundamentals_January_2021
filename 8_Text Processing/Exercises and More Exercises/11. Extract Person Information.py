for lines in range(int(input())):
    line = input().replace(" ", "").replace("", " ").split()
    current_name = [line[l] for l in range((line.index("@")) + 1, (line.index("|")))]
    current_age = [line[n] for n in range((line.index("#")) + 1, (line.index("*")))]
    print(f"{''.join(current_name)} is {''.join(current_age)} years old.")

