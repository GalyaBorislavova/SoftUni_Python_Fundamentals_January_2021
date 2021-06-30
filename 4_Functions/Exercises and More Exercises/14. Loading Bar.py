def print_loading_bar(number_of_percents):
    percent = number_of_percents # 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    if percent == 0:
        loading = "." * 10
        print(f"{int(percent)}% [{loading}]")
        print("Still loading...")
    elif 10 <= percent <= 90:
        loading = percent // 10
        loading_print_bar = "%" * loading
        end_points = 10 - loading
        end_bar = "." * end_points
        print(f"{percent}% [{loading_print_bar}{end_bar}]")
        print("Still loading...")
    elif percent == 100: # 100 %
        loading = percent // 10
        loading_print = "%" * loading
        print(f"{percent}% Complete!")
        print(f"[{loading_print}]")


number_charged = int(input())
print_loading_bar(number_charged)
#
# 50% [%%%%%.....]
# Still loading...
# 100% Complete!
# [%%%%%%%%%%]