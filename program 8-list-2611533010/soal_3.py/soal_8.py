number_of_rows = 4
seats_per_row = 5

# Buat denah 4 baris x 5 kursi dengan list terpisah untuk tiap baris
seats = [["." for _ in range(seats_per_row)] for _ in range(number_of_rows)]

while True:
    for row_idx in range(number_of_rows):
        print(f"Row {row_idx + 1}: " + " ".join(seats[row_idx]) + " ")

    row_input = int(input("Row (0 to stop): "))
    if row_input == 0:
        break

    seat_input = int(input("Seat: "))

    # Cek apakah nomor baris dan kursi berada di luar rentang (1..4 dan 1..5)
    if row_input < 1 or row_input > number_of_rows or seat_input < 1 or seat_input > seats_per_row:
        print("Invalid seat.")
        continue

    r = row_input - 1
    s = seat_input - 1

    # Cek apakah kursi sudah terisi 'X'
    if seats[r][s] == "X":
        print("Seat already taken.")
    else:
        seats[r][s] = "X"
        print("Seat booked.")

# Hitung total kursi yang terisi ('X')
seats_taken = 0
for row in seats:
    for cell in row:
        if cell == "X":
            seats_taken += 1

print(f"Seats taken: {seats_taken}")