print ("            Program penjualan tiket")
print ("               PT Atour Travel")
def numberformat(number):
    return "{:,}".format(int(number)).replace(',','.')
namapenumpang = input("Masukkan nama penumpang:  ")
#list
listkodepesawat = {
    "1":{
        "namapesawat":"Garuda Indonesia",
        "harga":2275000,
        "kota":"Denpasar"
    },
    "2":{
        "namapesawat":"Mandala",
        "harga":1330000,
        "kota":"Malang"
    },
    "3":{
        "namapesawat":"Merpati",
        "harga":1185000,
        "kota":"Surabaya"
    },
    "4":{
        "namapesawat":"Lion Air",
        "harga":1750000,
        "kota":"Pontianak"
    }
}
for i in listkodepesawat.keys():
    print(i,listkodepesawat[i]['namapesawat'],listkodepesawat[i]['harga'],listkodepesawat[i]['kota'])
# print([key for key in listkodepesawat[].keys()])
kodepesawat   = input("\nMasukkan nomor pesawat  :  ")
if kodepesawat in listkodepesawat:
    # print("Total bayar =" listkodepesawat[])
    jumlahtiket   = int(input("Masukkan jumlah tiket  :  "))
    jumlahbayar = listkodepesawat[kodepesawat]['harga'] * jumlahtiket
    ppn = 0.1*jumlahbayar
    totalbiaya = jumlahbayar + ppn
    print("Total biaya      ",numberformat(totalbiaya))
    uangbayar     = int(input("Masukkan uang bayar    :"))
    while uangbayar < totalbiaya:
        if uangbayar < totalbiaya:
            print("Harap masukkan uang pas atau lebih")
            uangbayar = int(input("uang bayar"))
            print("+++++++")
        # else:
    kembali = uangbayar - totalbiaya
    print("\n")
    print("Nama Penumpang",namapenumpang)
    print("Kode pesawat",kodepesawat)
    print("Jumlah tiket",jumlahtiket)
    print("\n")
    print("Pesawat yang dipilih   :",listkodepesawat[kodepesawat]['namapesawat'])
    print("Rincian penjualan tiket: ")
    print("________________")
    print("Kota yang dituju       :",listkodepesawat[kodepesawat]['kota'])
    print("Harga Tiket            :",numberformat(listkodepesawat[kodepesawat]['harga']))
    print("Jumlah bayar           :",numberformat(jumlahbayar))
    print("PPN                    :",numberformat(ppn))
    print("________________")
    print("Total Biaya            :",numberformat(totalbiaya))
    print("Uang Bayar             :",numberformat(uangbayar))
    print("Kembali                :",numberformat(kembali),'\n')
    # break
else:
    print("\nharap masukkan yang ada di list")

