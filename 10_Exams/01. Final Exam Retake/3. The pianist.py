pieces = {}
n = int(input())
for _ in range(n):
    current_piece = input().split("|")
    piece, composer, key = current_piece
    if piece not in pieces:
        pieces[piece] = {"Composer": composer,"Key": key}
command = input()

while not command == "Stop":
    command = command.split("|")
    action = command[0]
    piece = command[1]
    if action == "Add":
        composer = command[2]
        key = command[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"Composer": composer, "Key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = command[2]
        if piece in pieces:
            pieces[piece]['Key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for piece, c_k in sorted(pieces.items(), key=lambda x: (x[0], x[1]['Composer'])):
    print(f"{piece} -> Composer: {c_k['Composer']}, Key: {c_k['Key']}")