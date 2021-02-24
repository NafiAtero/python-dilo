class TempConv:

    tempIdx = ["Celsius","Kelvin","Reaumur","Fahrenheit"]

    def __init__(self,tempIn):
        self.tempIn = tempIn

    def selectedUnitFrom(self,unitIn):
        self.selectedUnitIn = self.tempIdx[unitIn - 1]
        del self.tempIdx[unitIn - 1]
        return self.selectedUnitIn

    def unselectedUnit1(self):
        return self.tempIdx[0]
    def unselectedUnit2(self):
        return self.tempIdx[1]
    def unselectedUnit3(self):
        return self.tempIdx[2]
    
    def selectedUnitTo(self,unitOut):
        return self.tempIdx[unitOut - 1]

    def convertToKelvin(self,unitIn):
        if unitIn == 1:
            self.kelvin = self.tempIn + 273 / 1
            return self.kelvin
        elif unitIn == 2:
            self.kelvin = self.tempIn
            return self.kelvin
        elif unitIn == 3:
            self.kelvin = (self.tempIn * 5/4) + 273
            return self.kelvin
        elif unitIn == 4:
            self.kelvin = ((self.tempIn- 32) * 5/9) + 273
            return self.kelvin

    def convertFromKelvin(self,kelvinIn,unitOut):
        #del self.tempIdx[unitIn - 1]
        if self.tempIdx[unitOut - 1] == "Celsius":
            return kelvinIn - 273 / 1
        elif self.tempIdx[unitOut - 1] == "Kelvin":
            return kelvinIn
        elif self.tempIdx[unitOut - 1] == "Reaumur":
            return (kelvinIn - 273) * 4/5
        elif self.tempIdx[unitOut - 1] == "Fahrenheit":
            return ((kelvinIn - 273) * 9/5 ) + 32

#Temp in invalid
def tempInInvalid():
    print("")
    inputTemp = input("Please input a number: ")
    if inputTemp.isdecimal:
        return int(inputTemp)
    else:
        tempInInvalid()


#Unit in
def unitInSelection():
    print("[1] Celsius")
    print("[2] Kelvin")
    print("[3] Reaumur")
    print("[4] Fahrenheit")

def unitInInvalid():
    print("")
    print(unitInSelection())
    unitIn = input("Please select a number between 1 and 4: ")

    if 1 <= int(unitIn) <= 4:
        return int(unitIn)
    else:
        unitInInvalid()

#Unit out
def unitOutSelection():
    print("[1] {}".format(conv.unselectedUnit1()))
    print("[2] {}".format(conv.unselectedUnit2()))
    print("[3] {}".format(conv.unselectedUnit3()))

def unitOutInvalid():
    print("")
    print(unitOutSelection())
    unitOut = input("Please select a number between 1 and 3: ")

    if 1 <= int(unitOut) <= 3:
        return int(unitOut)
    else:
        unitOutInvalid()


print("")

print("Temprature Converter v1.2")

print("")

#Input temp
inputTemp = input("Input number to convert: ")
if inputTemp.isnumeric():
    int(inputTemp)
else:
    tempInInvalid()

print("")

#Select in unit
"""
unitInSelection()
unitIn = input("Select temprature unit to convert from: ")
"""
#Unit in check

while True:
    try:
        unitInSelection()
        unitIn = int(input("Select temprature unit to convert from: "))
        break
    except:
        

"""
if 1 <= int(unitIn) <= 4:
    unitIn = int(unitIn)
else:
    unitIn = int(unitInInvalid())
"""

#Unit in fuctions
conv = TempConv(inputTemp)
unitInName = conv.selectedUnitFrom(unitIn)

print("")

#Select unit out
unitOutSelection()
unitOut = int(input("Select temprature unit to convert to: "))

#Unit out check
if 1 <= int(unitOut) <= 3:
    int(unitIn)    
else:
    unitOut = unitOutInvalid()

#Unit out functions
kelvinConverted = conv.convertToKelvin(unitIn)
#print(kelvinConverted)
#unitName = TempNames(unitIn,unitOut)

print("")

#Output
print("{} {} is {} {}".format(str(inputTemp),unitInName,conv.convertFromKelvin(kelvinConverted,unitOut),conv.selectedUnitTo(unitOut)))

print("")