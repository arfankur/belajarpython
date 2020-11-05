#fungsi garis
def garis():
    print(58*'=')

garis()
print("                   GEROBAK AYAM SUKSES")
garis()
print("               Kode  Jenis Potong   Harga")
garis()
print("                D        Dada       Rp. 12000")
print("                P        Paha       Rp. 10000")
print("                S        Sayap      Rp. 9000")
garis()

#fungsi list untuk penyimpanan data sementara
listkode=[]
listbanyak=[]

#nilai awal
jumbay=0
totbay=0

#input jumlah banyak data yang akan diulang (batas perulangan)
isi=int(input("Banyak Jenis : "))

#proses perulangan
for i in range(isi):
    garis()
    print ("Jenis ke - " , i+1)
    kode=input("Kode Potong [D/P/S] : ")
    listkode.append(kode)
    jum=int(input("Banyak Potong : "))
    listbanyak.append(jum)

#tampilan output
garis()
print("                   GEROBAK AYAM SUKSES")
garis()
print("No     Jenis        Harga           Banyak      Jumlah ")
print("       Potong       Satuan          Beli        Harga  ")
garis()

#operasi percabangan
for i in range(isi):
    if listkode[i] == "D" or listkode[i] == "d":
        jenis = "Dada"
        harga = 12000
    elif listkode[i] == "P" or listkode[i] == "p":
        jenis = "Paha"
        harga = 10000
    elif listkode[i] == "S" or listkode[i] == "s":
        jenis = "Sayap"
        harga = 9000
    else:
        jenis = "-"
        harga = 0

#operasi perhitungan
for i in range(isi):
    jumhar=listbanyak[i]*harga
    jumbay=jumbay+jumhar
    pajak=0.1*jumbay
    totbay=jumbay+pajak
    # pemanggilan tampilan hasil input
    print(i + 1, "     ", jenis, "      ", harga, "           ", listbanyak[i], "       ", jumhar)
    # continue
garis()
print("                            Jumlah Bayar : Rp. ", jumbay)
print("                            Pajak        : Rp. ", pajak)
print("                            Total  Bayar : Rp. ", totbay)