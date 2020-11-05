ulang = 2
res = []
for i in range(ulang):
    print ("data ke - " + str(i+1))
    nim=input("Masukkan Nim Mahasiswa:\t")
    uts=int(input("Masukkan Nilai UTS Mahasiswa:\t"))
    uas=int(input("Masukkan Nilai UAS Mahasiswa:\t"))
    print("NIM mahasiswa adalah %s Nilai UTS %i dan Nilai UAS %i"%(nim,uts,uas))
    print('===================================\n')
    a = nim[i]
res.extend(a)
print(res)