import sys
def numberformat(number):
    return "Rp {:,}".format(int(number)).replace(',','.')

listMenu = {
    "D":{
        "jenispotong": 'Dada',
        "harga": 2500,
    },
    "P":{
        "jenispotong": 'Paha',
        "harga": 2000
    },
    "S":{
        "jenispotong": 'Sayap',
        "harga": 1500
    }
}
start = 1
kodePotongan = []
hargaPotongan = []
jumlahPotongan = []
banyakBeli = []
jumlahHarga = []
jenisPotongan = []
tab = '\t'
inputJumlah = int(input("Masukkan jumlah \t"))
for i in range(inputJumlah):
    print('Kode Potongan\t','Jenis Potongan\t','Harga')
    print('= = = = = = = = = = = = = = = = = = = = = ')
    for menu in listMenu.keys():
        print(menu+ '\t\t',listMenu[menu]['jenispotong']+ '\t\t',numberformat(listMenu[menu]['harga'])+ '\t')
    inputKodePotongan = input("Masukkan kode potongan\t")
    if inputKodePotongan in listMenu:
        inputBanyak = int(input("Masukkan jumlah pesanan\t"))
        kodePotongan.append(inputKodePotongan)
        jenisPotongan.append(listMenu[inputKodePotongan]['jenispotong'])
        hargaPotongan.append(listMenu[inputKodePotongan]['harga'])
        banyakBeli.append(inputBanyak)
        jumlah = inputBanyak * listMenu[inputKodePotongan]['harga']
        jumlahHarga.append(jumlah)
        print(numberformat(inputBanyak * listMenu[inputKodePotongan]['harga']))
        i +=1
    else:
        sys.exit("Harap masukkan yyang ada di list")

    print('No','\t','Kode','\t','Jenis','\t','Harga','\t','Banyak ','\t','Jumlah')
    print('\t','Potongan','\t','Potongan','\t','Beli','\t','Harga')

for i in range(inputJumlah):
    print(i + 1,'\t',kodePotongan[i],'\t',jenisPotongan[i],'\t',hargaPotongan[i],'\t',banyakBeli[i],'\t',jumlahHarga[i])