print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. INPUT DATA PENGUNJUNG
nama_pengunjung_3010 = input("Masukkan Nama Pengunjung        : ")
umur_3010 = int(input("Input umur anda                 : "))
sim_3010 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
jumlah_tiket_3010 = int(input("Masukkan jumlah tiket           : "))

# Validasi jumlah tiket menggunakan if tunggal
if jumlah_tiket_3010 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")
    raise SystemExit


# 2. PEMILIHAN PAKET WAHANA MENGGUNAKAN MATCH-CASE
print("\nPilihan Paket Wahana (1-5):")
print(" 1. Safari Rimba         (Rp 50,000)")
print(" 2. Arung Jeram          (Rp 75,000)")
print(" 3. Motor ATV Ekstrim    (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp 100,000)")
print(" 5. All-Access VIP       (Rp 220,000)")

paket_3010 = int(input("Masukkan nomor paket (1-5) : "))

match paket_3010:
    case 1:
        nama_wahana_3010 = "Wahana Safari Rimba"
        harga_satuan_3010 = 50000
    case 2:
        nama_wahana_3010 = "Wahana Arung Jeram"
        harga_satuan_3010 = 75000
    case 3:
        nama_wahana_3010 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3010 = 120000
    case 4:
        nama_wahana_3010 = "Wahana Roller Coaster Kilat"
        harga_satuan_3010 = 100000
    case 5:
        nama_wahana_3010 = "Wahana All-Access VIP"
        harga_satuan_3010 = 220000
    case _:
        print("Paket wahana tidak valid!")
        raise SystemExit


# 3. VALIDASI IZIN KENDALI WAHANA
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_3010 == 3 and umur_3010 >= 17 and sim_3010 == 'y':
    status_akses_3010 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
elif paket_3010 == 3 and umur_3010 >= 17 and sim_3010 != 'y':
    status_akses_3010 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
elif paket_3010 == 3 and umur_3010 < 17 and sim_3010 == 'y':
    status_akses_3010 = "Identitas tidak valid: Belum cukup umur memiliki SIM."
elif paket_3010 == 3:
    status_akses_3010 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."
elif umur_3010 >= 10:
    status_akses_3010 = "Anda memenuhi syarat umur untuk wahana ini."
else:
    status_akses_3010 = "Anda belum cukup umur untuk wahana ini."

print(f"Status Akses: {status_akses_3010}")


# 4. INPUT DATA DISKON
is_member_3010 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_3010 = input("Apakah kode promo valid? (y/t) : ").strip().lower()


# 5. PERHITUNGAN SUBTOTAL
subtotal_3010 = harga_satuan_3010 * jumlah_tiket_3010


# 6. MULTI-IF UNTUK DISKON AKUMULATIF
total_diskon_persen_3010 = 0

if subtotal_3010 >= 200000:
    total_diskon_persen_3010 += 10

if is_member_3010 in ['y', 'ya']:
    total_diskon_persen_3010 += 5

if kode_promo_valid_3010 in ['y', 'ya']:
    total_diskon_persen_3010 += 15

if jumlah_tiket_3010 >= 5:
    total_diskon_persen_3010 += 5


# 7. PERHITUNGAN NOMINAL DISKON DAN TOTAL BAYAR
nominal_diskon_3010 = subtotal_3010 * (total_diskon_persen_3010 / 100)
total_bayar_3010 = subtotal_3010 - nominal_diskon_3010


# 8. EVALUASI KELULUSAN AUDIT
if total_bayar_3010 > 300000:
    catatan_layanan_3010 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_3010 = "Terima kasih telah berkunjung."


# 9. RINCIAN PEMBAYARAN
print("\n--- Rincian Pembayaran ---")
print(f"Nama Pengunjung  : {nama_pengunjung_3010}")
print(f"Wahana           : {nama_wahana_3010}")
print(f"Harga Satuan     : Rp {harga_satuan_3010:,.0f}".replace(",", "."))
print(f"Jumlah Tiket     : {jumlah_tiket_3010}")
print(f"Subtotal Belanja : Rp {subtotal_3010:,.0f}".replace(",", "."))
print(f"Total Diskon     : {total_diskon_persen_3010}% (Rp {nominal_diskon_3010:,.0f})".replace(",", "."))
print(f"Total Bayar      : Rp {total_bayar_3010:,.0f}".replace(",", "."))
print(f"Catatan Layanan  : {catatan_layanan_3010}")

print("\nProgram Selesai") 