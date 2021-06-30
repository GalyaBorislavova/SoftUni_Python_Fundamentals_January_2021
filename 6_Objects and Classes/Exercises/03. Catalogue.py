class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        match_first_letter = []
        for p in range(len(self.products)):
            if self.products[p][0] == first_letter:
                match_first_letter.append(self.products[p])
        return match_first_letter

    def __repr__(self):
        to_print = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{to_print}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
