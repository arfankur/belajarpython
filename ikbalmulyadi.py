from terminaltables import AsciiTable

numfor = lambda x : "{:,}".format(x).replace(',','.')
    
class Menu : 
    MenuList = {
    "D" : {
        "harga" : 35000,
        "label" : "Dada",
    },
    "P" : {
        "harga" : 10000,
        "label" : "Paha"
    },
    "S" : {
        "harga" : 30000,
        "label" : "Sayap",
        }
    }

    Menus = []

    def __init__(self,until = 3) : 
        for index in range(until) :
            self.ShowInput()
        self.cetak()

    def isExistMenu(self,type = "") : 
        return type.upper() in self.MenuList

    def ShowInput(self) :

        label =  input("Pilih Menu [D,P,S] : ")
        if self.isExistMenu(label) :
            self.Menus.append({ 
                "label" : label.upper(), 
                "jumlah" : int(input("Berapa Jumlah :")) 
            })
        else :
            self.ShowInput()
    pass

    def cetak(self) :
        table = [
            ['No', "Jenis Potong","Harga Satuan","Jumlah Harga"]
        ]
        total = 0


        for index,menu in enumerate(self.Menus) :
            
            listMenu = self.MenuList[menu['label']]

            total += menu['jumlah'] * listMenu['harga']

            table.append([index + 1, listMenu['label'],str(menu['jumlah']) + " Pcs",numfor(listMenu['harga'])])
        
        pajak = total - (total * 10 / 100)

        table.append(['','','','Jumlah Bayar :',numfor(total)])
        table.append(['','','','Total Pajak :',numfor(pajak)])
        table.append(['','','','Total Bayar :',numfor(total + pajak)])

        print(AsciiTable(table).table)
        exit()

Menu(int(input("Tambah Input :")))