total = 0

while True:
    num = int(input("Enter a number: "))
    
    if num < 0:
        break
    elif num == 0:
        continue
    else:
        print("Positive number:", num)
        total += num

print("Total:", total)