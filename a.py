#variable yg berulang menggunakan List/matriks 

nim=[]
uts=[]
uas=[]
total=[]

loop=2
for i in range(loop):
    print ("data Ke - " + str(i+1))
    nim.append(input("Masukkan Nim anda : "))
    uts.append(int(input("Masukkan Nilai UTS anda :"))) 
    uas.append(int(input("Masukkan Nilai UAS : ")))

#proses
for i in range(loop):
    total.append((uas[i] + uts[i]) / 2)
    
#Cetak 
print("=============================================================")  
print("Nim          Nilai Uts       Nilai UAS                 Total") 
print("=============================================================") 
for i in range(loop):
    print ("%s \t %i \t\t %i \t\t\t %i" % (nim[i],uts[i],uas[i],total[i]))
print("=============================================================")