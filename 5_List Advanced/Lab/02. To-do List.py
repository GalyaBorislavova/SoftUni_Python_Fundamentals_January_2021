notes = input().split("-")
list_task = [''] * 10

while "End" not in notes:
    importance = int(notes[0])
    index = importance - 1
    task = notes[1]
    list_task[index] = task

    notes = input().split("-")

to_do_list = [x for x in list_task if not x == '']
print(to_do_list)
