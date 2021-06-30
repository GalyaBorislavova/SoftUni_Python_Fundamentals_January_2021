def ticket_is_jackpot(t):
    for symbol in winning_symbols:
        if symbol * 20 in t:
            print(f"ticket \"{t}\" - 10{symbol} Jackpot!")
            return True
    return False


def win_ticket(t):
    left_half = t[:10]
    right_half = t[10:]
    for symbol in winning_symbols:
        if symbol * 6 in left_half and symbol * 6 in right_half:
            match_length = min(left_half.count(symbol), right_half.count(symbol))
            print(f"ticket \"{t}\" - {match_length}{symbol}")
            return True
    print(f"ticket \"{ticket}\" - no match")
    return False


tickets = [t.strip() for t in input().split(", ")]
winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    if not len(ticket) == 20:
        print("invalid ticket")
        continue
    if ticket_is_jackpot(ticket):
        continue
    if win_ticket(ticket):
        continue
