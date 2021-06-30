version_as_list = input().split(".")
version_as_int = int(''.join(version_as_list)) + 1
new_version = '.'.join(str(version_as_int))
print(new_version)
