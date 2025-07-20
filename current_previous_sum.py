previous_num = 0

print("Current  Previous  Sum")
for current_num in range(10):
    total = current_num + previous_num
    print(f"{current_num:<8} {previous_num:<9} {total}")
    previous_num = current_num
