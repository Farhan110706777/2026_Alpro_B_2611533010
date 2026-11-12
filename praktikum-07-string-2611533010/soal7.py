# Nama: Muhammad Farhan Amri
# NIM: 2611533010
# Pertanyaan 7

nama = "Muhammad Farhan Amri"
nim = "2611533010"

# Membuat username (nama depan huruf kecil + 3 digit terakhir NIM)
nama_pengguna = nama[:nama.find(" ")].lower() + nim[-3:]
asupan = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {nama}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {nama_pengguna}")
print(f"{'Intake':<10}: {asupan}")
print("=" * 30)