class Mobil:
    carJenis = ["SUV","Sedan","Minivan"]
    carMerk = ["Toyota","Honda","Jeep"]
    carWarna = ["Merah","Hitam","Putih"]

    def __init__(self):
        self.userChoice = {}

    def setJenis(self,_carJenis):
        self.userChoice["Jenis"] = self.carJenis[_carJenis - 1]

    def setMerk(self,_carMerk):
        self.userChoice["Merk"] = self.carMerk[_carMerk - 1]

    def setWarna(self,_carWarna):
        self.userChoice["Warna"] = self.carWarna[_carWarna - 1]

    def getResults(self):
        return self.userChoice

print("")

print("[1] SUV")
print("[2] Sedan")
print("[3] Minivan")
jenisIn = input("Pilih jenis mobil yang anda inginkan: ")

print("")

print("[1] Toyota")
print("[2] Honda")
print("[3] Jeep")
merkIn = input("Pilih jenis merk yang anda inginkan: ")

print("")

print("[1] Merah")
print("[2] Hitam")
print("[3] Putih")
warnaIn = input("Pilih jenis warna yang anda inginkan: ")

print("")

mobil = Mobil()
mobil.setJenis(int(jenisIn))
mobil.setMerk(int(merkIn))
mobil.setWarna(int(warnaIn))

#print(mobil.getResults())
jenis = mobil.getResults()["Jenis"]
merk = mobil.getResults()["Merk"]
warna = mobil.getResults()["Warna"]
print(f"Anda memilih mobil {jenis} bermerk {merk} dengan warna {warna}.")