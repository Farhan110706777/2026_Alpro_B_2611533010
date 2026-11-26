n = int(input())
kas = {}

for i in range(n):
    nama, uang = input().split()
    uang = int(uang)
    if nama not in kas:
        kas[nama] = 0
    kas[nama] += uang

for nama in kas:
    print(nama + ": " + str(kas[nama]))

print("Total cash:", sum(kas.values()))

terbesar = max(kas, key=kas.get)
print("Top contributor:", terbesar, "(" + str(kas[terbesar]) + ")")