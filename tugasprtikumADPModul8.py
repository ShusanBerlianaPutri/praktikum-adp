list_buku = [
    "9786020324875, Hujan               ,Tere Liye                ,9  ,52000 ,75000",
    "9786020324806, Laskar Pelangi      ,Andrea Hirata            ,15 ,50000 ,70000",
    "9786020324790, Ayat-Ayat Cinta     ,Habiburrahman El Shirazy ,3  ,60000 ,85000",
    "9786020324851, Pulang              ,Tere Liye                ,8  ,53000 ,73000",
    "9786022914020, Ayah                ,Andrea Hirata            ,7  ,53000 ,72000",
    "9786020323671, Rindu               ,Tere Liye                ,13 ,51000 ,75000",
    "9786024244902, Garis Waktu         ,Fiersa Besari            ,4  ,57000 ,77000",
    "9786020324684, Laut Bercerita      ,Leil S.Chudori           ,6  ,75000 ,95000",
    "9789797808518, Bumi                ,Tere Liye                ,12 ,60000 ,80000",
    "9786024248719, Sabtu Bersama Bapak ,Adhitua Mulya            ,7  ,60000 ,80000"
]
with open("inventaris_buku.txt","w") as file:
    file.write("ISBN,Judul,Penulis,Stok,Harga Beli,Harga Jual\n")
    for buku in list_buku:
        file.write(buku + "\n")
inventaris = {}
baris_ke = 0
with open("inventaris_buku.txt","r") as file:
   for line in file:
    if baris_ke == 0:
        baris_ke += 1
        continue
    data = []
    kata = " "
    for huruf in line :
        if huruf == "," or huruf == "\n" :
            data.append(kata)
            kata = " "
        else:
            kata += huruf
    isbn = data[0]
    inventaris[isbn] = {
        "judul" : data[1],
        "penulis" : data[2],
        "stok" : int(data[3]),
        "harga beli" : int(data[4]),
        "harga jual" : int(data[5])
    }
for isbn in inventaris :
    stok = inventaris[isbn]["stok"]
    harga_beli = inventaris[isbn]["harga beli"]
    harga_jual = inventaris[isbn]["harga jual"]
    potensi  = (harga_jual - harga_beli) * stok
    inventaris[isbn]["potensi keuntungan"] = potensi
with open("laporan_inventaris.txt","w") as file:
    file.write("ISBN,Judul,Penulis,Stok,Harga Beli,Harga Jual, Potensi Keuntungan \n")
    for isbn in inventaris:
        data = inventaris[isbn]
        file.write(
            isbn + ","+ data["judul"]+ ","+ data["penulis"] + "," + str(data["stok"]) + "," + str(data["harga beli"]) + "," + str(data["harga jual"]) +  "," + str(data["potensi keuntungan"])+ "\n"
        )
daftar_isbn = []
for key in inventaris :
    daftar_isbn.append(key)
isbn_awal = daftar_isbn[0]
maks_untung = inventaris[isbn_awal]["potensi keuntungan"]
min_untung = inventaris[isbn_awal]["potensi keuntungan"]
buku_maks = inventaris[isbn_awal]["judul"]
buku_min = inventaris[isbn_awal]["judul"]
for isbn in inventaris:
    potensi = inventaris[isbn]["potensi keuntungan"]
    if potensi > maks_untung:
        maks_untung = potensi 
        buku_maks = inventaris[isbn]["judul"]
    if potensi < min_untung:
        min_untung = potensi
        buku_min  = inventaris[isbn]["judul"]
print("potensi buku dengan keuntungan TERTINGGI:")
print(buku_maks, "=>  Rp." ,maks_untung)
print("\npotensi buku dengan keuntungan TERENDAH:")
print(buku_min, "=>  Rp." , min_untung)
total_nilai = 0
for isbn in inventaris:
    total_nilai += inventaris[isbn]["stok"]*inventaris[isbn]["harga beli"]
print("\n total nilai inventaris (berdasarkan harga beli):")
print( "Rp.", total_nilai)
print("\n stok buku KURANG dari 5 (segera direstock):")
for isbn in inventaris :
    stok = inventaris[isbn]["stok"]
    if stok < 5:
        print("-" + inventaris[isbn]["judul"], "=> stok:", stok)
