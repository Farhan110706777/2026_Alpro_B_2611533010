phone = "081234567890"
masked = phone[:4] + "*" * 5 + phone[-3:]
print(masked)


phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-3:]
print(masked)


phone = "0812345678"
masked = phone[:4] + "*" * 3 + phone[-3:]
print(masked)

phone = "082611533010"
masked = phone[:4] + "*" * 5 + phone[-3:]
print(masked)