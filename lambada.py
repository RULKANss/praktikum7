# List untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi lambda untuk setiap operasi
tambah = lambda nama, nilai: data_mahasiswa.append((nama, nilai)) if nama not in [mhs[0] for mhs in data_mahasiswa] else print(f"Mahasiswa dengan nama {nama} sudah ada.")

tampilkan = lambda: print("\n".join([f"Nama: {mhs[0]}, Nilai: {mhs[1]}" for mhs in data_mahasiswa]) if data_mahasiswa else "Belum ada data mahasiswa.")

hapus = lambda nama: data_mahasiswa.remove(next((mhs for mhs in data_mahasiswa if mhs[0] == nama), None)) if nama in [mhs[0] for mhs in data_mahasiswa] else print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

ubah = lambda nama, nilai_baru: next((data_mahasiswa.__setitem__(i, (nama, nilai_baru)) for i, mhs in enumerate(data_mahasiswa) if mhs[0] == nama), print(f"Mahasiswa dengan nama {nama} tidak ditemukan."))

# Menu interaktif
while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))
        tambah(nama, nilai)
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
        nilai_baru = float(input("Masukkan nilai baru: "))
        ubah(nama, nilai_baru)
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
