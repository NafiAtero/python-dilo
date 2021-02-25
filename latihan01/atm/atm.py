from datetime import datetime

class ATM:
    def __init__(self,saldo):
        self.saldo = saldo
        self.log = [f"Saldo awal anda Rp.{saldo}"]

    def storTunai(self,stor):
        self.saldo += stor
        time = datetime.now()
        time = time.strftime("%d/%m/%Y %H:%M:%S")
        self.log.append(f"{time}\nStor tunai Rp.{stor}\nSaldo anda Rp.{self.saldo}")


    def tarikTunai(self,tarik):
        if tarik <= self.saldo:
            self.saldo -= tarik
            time = datetime.now()
            time = time.strftime("%d/%m/%Y %H:%M:%S")    
            self.log.append(f"{time}\nTarik tunai Rp.{tarik}\nSaldo anda Rp.{self.saldo}")
        else:
            print("Saldo anda tidak mencukupi")

    def cetakResi(self):
        print("")
        for x in self.log:
            print(x)
            print("")

    def pilihJenisTransaksi(self):
        print("[1] Stor tunai")
        print("[2] Tarik tunai")
        print("[3] Lihat saldo")

        x = int(input("Pilih transaksi yang anda inginkan: "))

        if x == 1:
            stor = int(input("Masukan jumlah uang yang akan distorkan: Rp."))
            self.storTunai(stor)
            print(f"\nSisa saldo anda Rp.{self.saldo}\n")
        elif x == 2:
            tarik = int(input("Masukan Jumlah uang yang akan ditarik: Rp."))
            self.tarikTunai(tarik)
            print(f"\nSisa saldo anda Rp.{self.saldo}\n")
        elif x == 3:
            print(f"\nSisa saldo anda Rp.{self.saldo}\n")
        
        lagi = input("Apakah anda ingin melakukan transaksi lagi? [y/n] ")
        if lagi == "y":
            self.pilihJenisTransaksi()
        else:
            cetak = input("Apakah anda ingin mencetak resi? [y/n] ")
            if cetak == "y":
                self.cetakResi()

saldo = 1000000
atm = ATM(saldo)

print("\nSelamat datang di ATM\n")

atm.pilihJenisTransaksi()

print("")

print("Terima Kasih")

print("")