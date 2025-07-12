#Modul Eksternal
import csv
from datetime import datetime
import os

# Membuat file CSV jika belum ada atau masih kosong
def buat_file_csv():
    if not os.path.exists("keuangan.csv") or os.stat("keuangan.csv").st_size == 0:
        with open("keuangan.csv", "w", newline="") as file:
            tulis = csv.writer(file)
            tulis.writerow(["tanggal", "jenis", "kategori", "jumlah"])

# Validasi input tanggal
def input_tanggal():
    while True:
        tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
        try:
            datetime.strptime(tanggal, "%Y-%m-%d")
            return tanggal
        except:
            print(" Format salah! Contoh: 2025-07-06")

# Menambah transaksi keuangan
def tambah_transaksi():
    tanggal = input_tanggal()

    # Input ulang sampai jenis valid
    while True:
        jenis = input("Jenis transaksi (pemasukan/pengeluaran): ").lower()
        if jenis in ["pemasukan", "pengeluaran"]:
            break
        print(" Hanya boleh 'pemasukan' atau 'pengeluaran'.")

    kategori = input("Kategori (makan, transport, hiburan, dll): ")

    # Input ulang sampai jumlah valid
    while True:
        try:
            jumlah = float(input("Jumlah uang: "))
            break
        except:
            print(" Jumlah harus angka.")

    with open("keuangan.csv", "a", newline="") as file:
        tulis = csv.writer(file)
        tulis.writerow([tanggal, jenis, kategori, jumlah])
    
    print(f" Transaksi {jenis} sebesar Rp {jumlah:,.2f} berhasil disimpan.")

# Menampilkan pengeluaran terbesar
def pengeluaran_terbesar():
    data = {}
    with open("keuangan.csv", "r") as file:
        baca = csv.reader(file)
        next(baca)
        for baris in baca:
            if baris[1] == "pengeluaran":
                kategori = baris[2]
                jumlah = float(baris[3])
                if kategori in data:
                    data[kategori] += jumlah
                else:
                    data[kategori] = jumlah
    if data:
        terbesar = max(data, key=data.get)
        print(f" Pengeluaran terbesar: {terbesar} sebesar Rp {data[terbesar]:,.2f}")
    else:
        print(" Belum ada pengeluaran.")

# Menghitung saldo akhir
def cek_saldo():
    saldo = 0
    with open("keuangan.csv", "r") as file:
        baca = csv.reader(file)
        next(baca)
        for baris in baca:
            jumlah = float(baris[3])
            if baris[1] == "pemasukan":
                saldo += jumlah
            elif baris[1] == "pengeluaran":
                saldo -= jumlah
    print(f" Saldo akhir saat ini: Rp {saldo:,.2f}")

# Menu utama aplikasi
def menu():
    while True:
        print("\n=== MENU CEKSALDO ===")
        print("1. Tambah Transaksi")
        print("2. Lihat Pengeluaran Terbesar")
        print("3. Cek Saldo Akhir")
        print("4. Keluar")
        print("========================")
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == "1":
            tambah_transaksi()
        elif pilihan == "2":
            pengeluaran_terbesar()
        elif pilihan == "3":
            cek_saldo()
        elif pilihan == "4":
            print(" Program selesai. Terima kasih telah memakai aplikasi ini")
            break
        else:
            print(" Pilihan tidak ada.")

# Jalankan program
buat_file_csv()
menu()
