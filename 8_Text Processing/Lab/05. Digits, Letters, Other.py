data = input()
separator = "\n"
print(separator.join([''.join(filter(lambda x: x.isdigit(), data)),
                      ''.join(filter(lambda x: x.isalpha(), data)),
                      ''.join(filter(lambda x: not x.isdigit() and not x.isalpha(), data))]))