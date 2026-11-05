pin = input("Enter PIN: ")
correct_pin = "1234"
attempt = 1
MAX_ATTEMPTS = 3

if pin == correct_pin:
    print("Access granted")
else:
    while pin != correct_pin and attempt < MAX_ATTEMPTS:
        print("Incorrect PIN.")
        attempt += 1
print("Account locked")