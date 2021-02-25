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

    def __init__(self):
        self.barangDipilih = []
        self.uang = None

    def pilihanBarang(self):
        self.n = 1
        for x in self.items:
            nama = x.get("nama")
            harga = x.get("harga")
            satuan = x.get("satuan")
            
            print(f"[{self.n}] {nama} (Rp.{harga} per {satuan})")
            self.n += 1
        
    def validasiPilihan(self):
        self.pilihanBarang()
        print(f"[{self.n}] Selesai")
        pilihan = int(input("Pilih barang yang anda inginkan: ")) - 1
        


        if pilihan < self.n - 1:
            banyak = int(input(f"Pilih banyaknya: "))

            self.getItem(pilihan,banyak)
            print("")
            print(f"Total anda sekarang: Rp.{self.getHargaTotal()}")
            print("")
            self.validasiPilihan()

        elif pilihan == self.n - 1:
            print(f"Total anda: Rp.{self.getHargaTotal()}")

        else:
            print(f"Masukan angka 1-{self.n}")
            self.validasiPilihan()


    def getItem(self,pilihan,banyak):
        dictDipilih = self.items[pilihan]
        dictDipilih["banyak"] = banyak
        self.barangDipilih.append(dictDipilih)
        
    def getHargaTotal(self):
        self.total = 0
        for x in self.barangDipilih:
            harga = x.get("harga")
            banyak = x.get("banyak")
            self.total += harga * banyak
        return self.total

    def getKembalian(self,uang):
        return uang - self.total


toko = Toko()


print("")
print("Selamat datang di toko!")
print("")

toko.pilihanBarang()

print("")

pilihan = int(input("Pilih barang yang anda inginkan: ")) - 1

if pilihan < toko.n - 1:
    banyak = int(input(f"Pilih banyaknya: "))

    toko.getItem(pilihan,banyak)

    print("")
    print(f"Total anda sekarang: Rp.{toko.getHargaTotal()}")
    print("")

else:
    print(f"Masukan angka 1-{toko.n}")

toko.validasiPilihan()

print("")

uang = int(input("Masukan jumlah uang yang anda punya: Rp."))

print("")

kembalian = toko.getKembalian(uang)

if kembalian < 0:
    print("Uang anda kurang")
elif kembalian == 0:
    print("Uang anda pas")
else:
    print(f"Kembalian anda Rp.{kembalian}")

print("")

print("Terima Kasih!")