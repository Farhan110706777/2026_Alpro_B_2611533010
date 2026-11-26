schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

terbanyak = ""
maks = 0
for hari in schedule:
    if len(schedule[hari]) > maks:
        maks = len(schedule[hari])
        terbanyak = hari
print("Busiest day:", terbanyak, "(" + str(maks) + " courses)")

nama = input()
hitung = 0
for hari in schedule:
    if nama in schedule[hari]:
        hitung += 1
print(nama + ": " + str(hitung) + " days")