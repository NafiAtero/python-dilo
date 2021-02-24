class Toko:

    items = [{
        "nama": "Tissue",
        "harga": 2000,
        "satuan": "bungkus"
    },
    {
        "nama": "Lilin",
        "harga": 1000,
        "satuan": "batang"
    },
    {
        "nama": "Sabun",
        "harga": 3000,
        "satuan": "box"
    },
    {
        "nama": "Gula",
        "harga": 10000,
        "satuan": "kg"
    }
    ]

    #item = ["Tissue","Lilin","Sabun","Gula"]
    #harga = [2000,1000,3000,10000]
    #satuan = ["box","batang","batang","kg"]

    def __init__(self):
        self.barangDipilih = []
        self.uang = None

    def pilihanBarang(self):

        print(f"[1] {self.items[0]}")
        #print(f"[2] {self.item[1]} (Rp.{str(self.harga[1])} per {self.satuan[1]})")
        #print(f"[3] {self.item[2]} (Rp.{str(self.harga[2])} per {self.satuan[2]})")
        #print(f"[4] {self.item[3]} (Rp.{str(self.harga[3])} per {self.satuan[3]})")
        print("[11] Selesai")

    def getItem(self,pilihan):
        self.barangDipilih.append(self.item[pilihan])


    def getHargaTotal(self,barang,banyak):
        self.total = self.total + (self.harga[barang] * banyak)
        return self.total

    def getKembalian(self,uang):
        return uang - self.total





def pilihBarang():
    toko.pilihanBarang()
    pilihan = int(input("Pilih barang yang anda inginkan: ")) - 1
    #print(hargaTotal)

    if 0 <= pilihan <= 9:

        barang = toko.items[pilihan]
        hargaBarang = toko.harga[pilihan]
        satuanBarang = toko.satuan[pilihan]

        banyakBarang = int(input(f"Pilih banyaknya (Rp.{hargaBarang} per {satuanBarang}): "))
        #func
        testList1.append(barang)
        testList2.append(banyakBarang)
        total = toko.getHargaTotal(pilihan,banyakBarang)

        print("")
        print(f"Total anda sekarang Rp.{total}")

        print("")
        pilihBarang()
    
    elif pilihan == 10:
        print("")
        print(f"Total anda Rp.{total}")
        return None

    else:
        print("Masukan angka 1-11")

    

testList1 = []
testList2 = []
toko = Toko()



print("")
print("Selamat datang di toko!")
print("")
pilihBarang()
uang = int(input("Masukan jumlah uang yang anda punya: Rp."))
print("")

"""
print(testList1)
print(testList2)
print(toko.total)"""

kembalian = toko.getKembalian(uang)

if kembalian < 0:
    print("Uang anda kurang")
else:
    print(f"Kembalian anda Rp.{kembalian}")