import time
import os
from termcolor import colored,cprint

FILE_USERS = "users.txt"

def tampilkan_logo_bioskop():
    logo_lines = [
        "                                SELAMAT DATANG DI"
        "",
        "                                 █████╗ ███████╗",
        "                                ██╔══██╗██╔════╝",
        "                                ███████║███████╗",
        "                                ██╔══██║╚════██║",
        "                                ██║  ██║███████║",
        "                                ╚═╝  ╚═╝╚══════╝",
        "",
        "                                    BIOSKOP"
    ]
    
    for line in logo_lines:
        cprint(line, "cyan", attrs=["bold"])
        time.sleep(1)  # jeda 0.2 detik antar baris (bisa diubah sesuai selera)

def clear_screen():
    os.system("cls")

locations = {
    "CGV Raya Padang": [
        {"id": 1, "nama": "Avengers: Endgame", "studio": "Studio 1", "jam": "18:00", "harga": 50000},
        {"id": 2, "nama": "Spider-Man: No Way Home", "studio": "Studio 2", "jam": "20:00", "harga": 60000},
        {"id": 3, "nama": "Arwah","studio":"studio 3","jam":"10.00","harga":55000},
        {"id": 4, "nama": "Jalan Pulang","studio":"studio 4","jam":"13.00","harga":50000}
    ],
    "Plaza Andalas XXI": [
        {"id": 5, "nama": "Jumanji: The Next Level", "studio": "Studio 1", "jam": "19:00", "harga": 45000},
        {"id": 6, "nama": "Frozen II", "studio": "Studio 3", "jam": "21:00", "harga": 60000},
        {"id": 7, "nama": "Jumbo", "studio": "Studio 2", "jam": "17.00", "harga": 50000},
        {"id": 8, "nama": "Tak Ingin Usai Disini", "studio": "Studio 4", "jam": "08:00", "harga": 55000}
    ]
}
kursi_per_film = {}

def unit_kursi():
    for loc in locations.values():
        for film in loc:
            kursi_per_film[film["id"]] = [[False]*5 for _ in range(5)]

def animasi_loading(teks="Loading", detik=3):
    for _ in range(detik):
        for titik in ['.', '..', '...']:
            print(f"\r{teks}{titik}", end="", flush=True)
            time.sleep(0.5)
    print("\r" + " "*20, end="\r")

def baca_users():
    users = {}
    try:
        with open (FILE_USERS,"r") as f:
            for line in f:
                if line.strip():
                    nama, pw = line.strip().split(",")
                    users[nama] = pw 
    except FileNotFoundError:
        pass
    return users

def simpan_user(nama, pw):
    with open(FILE_USERS, "a") as f:
        f.write(f"{nama},{pw}\n")

def daftar():
    cprint("\n=== Daftar Akun Baru ===", "cyan", attrs = ["bold"])
    users = baca_users()
    while True:
        nama = input("Masukkan username: ").strip()
        if not nama:
            cprint("Username tidak boleh kosong.", "red")
            continue
        if nama in users:
            cprint("Username sudah terdaftar, coba yang lain.", "red")
        else:
            break
    while True:
        pw = input("Masukkan password: ").strip()
        if not pw:
            cprint("Password tidak boleh kosong.","red")
        else:
            break
    simpan_user(nama, pw)
    cprint("Pendaftaran berhasil! Silakan login.", "green")
    animasi_loading()

def login():
    cprint("\n=== Login ===", "cyan", attrs = ["bold"])
    users = baca_users()
    for _ in range(3):
        nama = input("Username: ").strip()
        pw = input("Password: ").strip()
        if nama in users and users[nama] == pw:
            cprint(f"Login berhasil. Selamat datang, {nama}!","green")
            animasi_loading()
            return nama
        else:
            cprint("Username atau password salah. Coba lagi.","red")
    cprint("Gagal login setelah 3 kali percobaan.","red")
    return None

def pilih_lokasi():
    cprint("\n=== Pilih Lokasi Bioskop ===","cyan", attrs = ["bold"])
    lokasi_list = list(locations.keys())
    for i in range(len(lokasi_list)):
        cprint(f"{i+1}.{lokasi_list[i]}","yellow")
    while True:
        try:
            pilih = int(input("Pilih lokasi (angka): "))
            if 1 <= pilih <= len(lokasi_list):
                return lokasi_list[pilih-1]
            else:
                cprint("Pilihan tidak valid.","red")
        except ValueError:
            cprint("Input harus angka.", "red")

def tampilkan_films(lokasi):
    cprint(f"\n=== Daftar Film di {lokasi} ===","cyan", attrs = ["bold"])
    print(f"{'ID':<3} {'Nama Film':<30} {'Studio':<10} {'Jam':<6} {'Harga':>7}")
    print("-"*60)
    for f in locations[lokasi]:
        print(f"{f['id']:<3} {f['nama']:<30} {f['studio']:<10} {f['jam']:<6} Rp{f['harga']:>6,}")

def tampilkan_kursi(film_id):
    cprint("\n=== Denah Kursi (O=tersedia, X=sudah dipesan) ===","cyan",attrs = ["bold"])
    print("-----------------------")
    print("   | 1 | 2 | 3 | 4 | 5 | ")
    print("-----------------------")
    for i in range(5):
        baris = kursi_per_film[film_id][i]
        baris_str = " "
        for kursi in baris :
            if kursi :
                baris_str += "X   "
            else:
                baris_str += "O   "
        print(f"{i+1:<3}| {baris_str.strip()} |")
        print("-----------------------")

def pilih_kursi(film_id, jumlah):
    kursi_dipilih = []
    for n in range(jumlah):
        while True:
            try:
                cprint(f"\nPilih kursi ke-{n+1}:","yellow")
                baris = int(input("  Masukkan nomor baris (1-5): ")) - 1
                kolom = int(input("  Masukkan nomor kolom (1-5): ")) - 1
                if baris not in range(5) or kolom not in range(5):
                    cprint("  Input kursi di luar jangkauan. Coba lagi.","red")
                    continue
                if kursi_per_film[film_id][baris][kolom]:
                    cprint("  Kursi sudah dipesan. Pilih kursi lain.","red")
                    continue
                if (baris, kolom) in kursi_dipilih:
                    cprint("  Kursi sudah Anda pilih sebelumnya.","red")
                    continue
                kursi_dipilih.append((baris, kolom))
                cprint(f"  Kursi baris {baris+1} kolom {kolom+1} berhasil dipilih.","green")
                break
            except ValueError:
                cprint("  Input tidak valid, masukkan angka.","red")
    return kursi_dipilih

def cetak_tiket_ke_file(username,lokasi,film,kursi,total_bayar,bayar,kembalian):
    nama_file = f"{username}_tiket.txt"
    with open(nama_file, "w") as f :
        f.write("================= Tiket Digital Anda ====================\n")
        f.write(f"Nama Pemesanan  : {username}\n")
        f.write(f"Lokasi          : {lokasi}\n")
        f.write(f"Film            : {film["nama"]}\n")
        f.write(f"Studio          : {film["studio"]}\n")
        f.write(f"Jam Tayang      : {film["jam"]}\n")
        b,k = kursi 
        f.write(f"kursi           : baris{b+1} kolom{k+1}\n")
        f.write(f"Total Bayar     : Rp{total_bayar:,}\n")
        f.write(f"Bayar           : Rp{bayar:,}\n")
        f.write(f"kembalian       : Rp{kembalian:,}\n")
        f.write("Terima Kasih Telah Memesan Tiket! Selamatt Menonton :\n")
        f.write("=========================================================")
    
def konfirmasi_pesanan(username):
    clear_screen()
    lokasi = pilih_lokasi()
    tampilkan_films(lokasi)
    while True:
        try:
            film_id = int(input("\nMasukkan ID film yang ingin dipesan: "))
            film = None
            for f in locations[lokasi]:
                if f["id"] == film_id:
                    film = f
                    break
            if film is None:
                cprint("ID film tidak valid. Coba lagi.","red")
                continue
            break
        except ValueError:
            cprint("Input tidak valid, masukkan angka.","red")

    tampilkan_kursi(film_id)
    while True:
        try:
            jumlah = int(input("Masukkan jumlah tiket yang ingin dipesan (max 5): "))
            if 1 <= jumlah <= 5:
                break
            else:
                cprint("Jumlah tiket minimal 1 dan maksimal 5.","red")
        except ValueError:
            cprint("Input tidak valid, masukkan angka.","red")

    kursi_dipilih = pilih_kursi(film_id, jumlah)
    total_bayar = film["harga"] * jumlah
    while True :
        try:
            bayar = int(input("Masukkan jumlah pembayaran: Rp"))
            if bayar < total_bayar:
                cprint("uang pembayaraan kurang.", "red")
                continue
            break
        except ValueError:
            cprint("input tidak valid, masukkan angka. ", "red")

    kembalian = bayar - total_bayar
    for i in range(len(kursi_dipilih)):
        b,k = kursi_dipilih[i]
        kursi_per_film[film_id][b][k] = True
        bayar_per_tiket = bayar//jumlah
        kembalian_per_tiket = bayar_per_tiket - film["harga"]
        cetak_tiket_ke_file(username,lokasi,film,(b,k),film["harga"], bayar_per_tiket,kembalian_per_tiket,i)
    animasi_loading("mencetak tiket",3)
    cprint("\nTiket Anda telah dicetak ke file! selamat menonton :", "cyan")

def main():
    unit_kursi()
    cprint("=== Sistem Pemesanan Tiket Bioskop Online ===","cyan",attrs = ["bold"])
    while True:
        cprint("\nMenu:","cyan", attrs = ["bold"])
        cprint("1. Daftar Akun Baru","yellow")
        cprint("2. Login","yellow")
        cprint("3. Keluar","red")
        pilihan = input("Pilih menu (1/2/3): ").strip()
        if pilihan == "1":
            daftar()
        elif pilihan == "2":
            user = login()
            if user:
                konfirmasi_pesanan(user)
        elif pilihan == "3":
            cprint("Terima kasih telah memesan tiket kami, sampai jumpaa!","cyan")
            break
        else:
            cprint("Pilihan tidak valid.","red")
clear_screen()
tampilkan_logo_bioskop()
clear_screen()
main()