mail = {}
capacity = int(input())
command = input()

while not command == "Statistics":
    command = command.split("=")
    action = command[0]
    if action == "Add":
        username = command[1]
        sent = int(command[2])
        received = int(command[3])
        if username not in mail:
            mail[username] = {"Sent": sent, "Received": received, "All": sent + received}
    elif action == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in mail and receiver in mail:
            if mail[sender]["All"] + 1 >= capacity or mail[receiver]["All"] + 1 >= capacity:
                if mail[sender]["All"] + 1 >= capacity:
                    del mail[sender]
                    print(f"{sender} reached the capacity!")
                if mail[receiver]["All"] + 1 >= capacity:
                    del mail[receiver]
                    print(f"{receiver} reached the capacity!")
            else:
                mail[sender]["Sent"] += 1
                mail[sender]["All"] += 1
                mail[receiver]["Received"] += 1
                mail[receiver]["All"] += 1
    elif action == "Empty":
        username = command[1]
        if username == "All":
            mail = {}
        elif username in mail:
            del mail[username]
    command = input()

print(f"Users count: {len(mail)}")
for person, mails in sorted(mail.items(), key=lambda x: (-x[1]["Received"], x[0])):
    print(f"{person} - {mails['All']}")
