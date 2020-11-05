nis     = input("input nis              :   ")
nama    = input("input nama             :   ")
jurusan = input("input jurusan [SI/SIA] :   ")
listJurusan = {
    "SI":{
        "namaprodi":"Sistem Informasi",
        "harga":2400000
    },
    "SIA":{
        "namaprodi":"Sistem Informasi Akuntansi",
        "harga":2000000
    },
}
if jurusan in listJurusan:
    print("\n")
    print("Jurusan      ",jurusan)
    print("Nama Prodi   ",listJurusan[jurusan]["namaprodi"])
    print("Harga        ",listJurusan[jurusan]["harga"])
else:
    print("\nharap masukkan yang ada di list")



    