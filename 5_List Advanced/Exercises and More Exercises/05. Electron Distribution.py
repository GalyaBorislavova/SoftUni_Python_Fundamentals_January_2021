electrons = int(input())
atom_shell = []
shell = 1

while electrons > 0:
    max_electrons = 2 * shell ** 2
    if electrons - max_electrons > 0:
        atom_shell.append(max_electrons)
        electrons -= max_electrons
        shell += 1
    else:
        break
atom_shell.append(abs(electrons))
print(atom_shell)