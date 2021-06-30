import re

pattern_valid_barcodes = r"(@(#{1,}))([A-Z][a-zA-Z0-9]{4,}[A-Z]\b)(@(#{1,}))"
pattern_product_group = r"\d"
n = int(input())
for _ in range(n):
    barcode = input()
    valid = [match.group() for match in re.finditer(pattern_valid_barcodes, barcode)]
    if valid:
        numbers_in_barcode = [i for i in re.findall(pattern_product_group, barcode)]
        if numbers_in_barcode:
            product_group = ''.join(numbers_in_barcode)
        else:
            product_group = f"00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
