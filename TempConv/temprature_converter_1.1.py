class TempNames:
    tempIdx = ["Celsius","Kelvin","Reaumur","Fahrenheit"]

    def __init__(self,tempUnitIn,tempUnitOut):
        self.tempUnitIn = tempUnitIn
        self.tempUnitOut = tempUnitOut

    def selectedUnitFrom(self):
        self.selectedUnitIn = self.tempIdx[self.tempUnitIn - 1]
        del self.tempIdx[self.tempUnitIn - 1]
        return self.selectedUnitIn

    def unselectedUnit1(self):
        return self.tempIdx[0]
    def unselectedUnit2(self):
        return self.tempIdx[1]
    def unselectedUnit3(self):
        return self.tempIdx[2]
    
    def selectedUnitTo(self):
        return self.tempIdx[self.tempUnitOut - 1]


class TempConv:

    tempIdx = ["Celsius","Kelvin","Reaumur","Fahrenheit"]

    def __init__(self,tempIn,tempUnitIn,tempUnitOut):
        self.tempIn = tempIn
        self.tempUnitIn = tempUnitIn
        self.tempUnitOut = tempUnitOut

    def convertToKelvin(self):
        if self.tempUnitIn == 1:
            self.kelvin = self.tempIn + 273 / 1
            return self.kelvin
        elif self.tempUnitIn == 2:
            self.kelvin = self.tempIn
            return self.kelvin
        elif self.tempUnitIn == 3:
            self.kelvin = (self.tempIn * 5/4) + 273
            return self.kelvin
        elif self.tempUnitIn == 4:
            self.kelvin = ((self.tempIn- 32) * 5/9) + 273
            return self.kelvin

    def convertFromKelvin(self):
        del self.tempIdx[self.tempUnitIn - 1]
        if self.tempIdx[self.tempUnitOut - 1] == "Celsius":
            return self.kelvin - 273 / 1
        elif self.tempIdx[self.tempUnitOut - 1] == "Kelvin":
            return self.kelvin
        elif self.tempIdx[self.tempUnitOut - 1] == "Reaumur":
            return (self.kelvin - 273) * 4/5
        elif self.tempIdx[self.tempUnitOut - 1] == "Fahrenheit":
            return ((self.kelvin - 273) * 9/5 ) + 32

print("")

print("Temprature Converter v1.1")
print("")
inputTemp = int(input("Input number to convert: "))

print("")

print("[1] Celsius")
print("[2] Kelvin")
print("[3] Reaumur")
print("[4] Fahrenheit")
unitIn = int(input("Select temprature unit to convert from: "))

unitName = TempNames(unitIn,0)
unitInName = unitName.selectedUnitFrom()

print("")

print("[1] {}".format(unitName.unselectedUnit1()))
print("[2] {}".format(unitName.unselectedUnit2()))
print("[3] {}".format(unitName.unselectedUnit3()))
unitOut = int(input("Select temprature unit to convert to: "))

convert = TempConv(inputTemp,unitIn,unitOut)
kelvinConverted = convert.convertToKelvin()
unitName = TempNames(unitIn,unitOut)

print("")

print("{} {} is {} {}".format(str(inputTemp),unitInName,convert.convertFromKelvin(),unitName.selectedUnitTo()))

print("")