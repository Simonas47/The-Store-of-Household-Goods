from FridgesRegister import FridgesRegister
from Fridge import Fridge
import csv
class InOutUtils:
    def ReadFridges (self, fileName: str): # reads information from file, stores it
        fridges = FridgesRegister()
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            count = 0
            for row in csv_reader:
                if count == 0:
                    shop = row[0]
                    count += 1
                elif count == 1:
                    address = row[0]
                    count += 1
                elif count == 2:
                    phoneNumber = row[0]
                    fridges.PutShop(shop, address, phoneNumber)
                    count += 1
                else:
                    name = row[0]
                    id = row[1]
                    volume = int(row[2])
                    energyClass = row[3]
                    installation = row[4]
                    color = row[5]
                    freezer = row[6]
                    price = float(row[7])
                    height = float(row[8])
                    width = float(row[9])
                    depth = float(row[10])

                    fridge = Fridge(name, id, volume, energyClass, installation, color, freezer, price, height, width, depth)
                    if not fridges.Contains(fridge):
                        fridges.Add(fridge)
        return fridges

    def PrintInitialData (self, register1: FridgesRegister, register2: FridgesRegister): # prints initial data to a file
        file = open('pradiniai_duomenys.txt', "w")
        text = "| {:>14} | {:>14} | {:>12} | {:>12} | {:>8} | {:>10} | {:>12} | {:>17} | {:>8} | {:>20} | {:>10} | {:>9} | {:>8} | {:>8} |"
        file.write('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        file.write(text.format("Shop name", "Address", "Phone Number","Manufacturer", "Model", "Volume (l)", "Energy class", "Installation type", "Color", "''Has a freezer?''", "Price, eur", "Height, m","Width, m", "Depth, m"))
        file.write('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        for i in range(register1.FridgesCount()):
            d = register1.GetFridge(i)
            file.write(text.format(register1.GetShop(), register1.GetAddress(), register1.getPhoneNumber(), d.name, d.id, d.volume, d.energyClass,
                                   d.installation, d.color, d.freezer, d.price, d.height, d.width, d.depth))
            file.write("\n")
        file.write('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        file.write("\n")


        file.write('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        file.write(text.format("Shop name", "Address", "Phone Number","Manufacturer", "Model", "Volume (l)", "Energy class", "Installation type", "Color", "''Has a freezer?''", "Price, eur", "Height, m","Width, m", "Depth, m"))
        file.write('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        for i in range(register2.FridgesCount()):
            d = register2.GetFridge(i)
            file.write(text.format(register2.GetShop(), register2.GetAddress(), register2.getPhoneNumber(), d.name, d.id, d.volume, d.energyClass,
                                   d.installation, d.color, d.freezer, d.price, d.height, d.width, d.depth))
            file.write("\n")
        file.write('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        file.write("\n")
        file.close()

    def PrintMostExpensiveFridges (self, register1: FridgesRegister, register2: FridgesRegister):
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
        text = "| {:>12} | {:>8} | {:>10} | {:>12} | {:>17} | {:>8} | {:>20} | {:>10} | {:>9} | {:>8} | {:>8} |"
        print(text.format("Manufacturer", "Model", "Volume (l)", "Energy class",
                        "Installation type", "Color", "''Has a freezer?''", "Price, eur", "Height, m", "Width, m",
                        "Depth, m"))
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
        text2 = '| {:>12} | {:>8} | {:>10} | {:>12} | {:>17} | {:>8} | {:>20} | {:>10} | {:>9} | {:>8} | {:>8} |'
        if register1.HighestCost() >= register2.HighestCost():
            for i in range(register1.FridgesCount()):
                fridge = register1.GetFridge(i)
                if fridge.volume >= 80 and fridge.price == register1.HighestCost():
                    print(text2.format(fridge.name, fridge.id, fridge.volume, fridge.energyClass, fridge.installation, fridge.color, fridge.freezer, fridge.price,
                                       fridge.height, fridge.width, fridge.depth))

        if register1.HighestCost() <= register2.HighestCost():
            for i in range(register2.FridgesCount()):
                fridge = register2.GetFridge(i)
                if fridge.volume >= 80 and fridge.price == register2.HighestCost():
                    print(text2.format(fridge.name, fridge.id, fridge.volume, fridge.energyClass, fridge.installation, fridge.color, fridge.freezer, fridge.price,
                                       fridge.height, fridge.width, fridge.depth))
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

    def PrintMostExpensiveManufacturer (self, register: FridgesRegister):
        print("The most expensive fridge's manufacurer(s) in the shop ''{}'' is (are):".format(register.GetShop()))
        for i in range(register.FridgesCount()):
            fridge = register.GetFridge(i)
            if register.HighestManufacturerCost() == fridge.price:
                print(fridge.name)

    def PrintExclusiveManufacturers(self, fileName, register1: FridgesRegister, register2:FridgesRegister):
        a = register1.FindExclusiveManufacturers(register2)

        csv.register_dialect('myDialect', delimiter=';', quoting=csv.QUOTE_NONE)
        with open(fileName, 'w', newline='') as file:
            writer = csv.writer(file, dialect='myDialect')
            writer.writerow(['Manufacturer', 'Shop'])

            for i in range(a.FridgesCount()):
                fridge = a.GetFridge(i)
                if not (register1.ExclusiveShopName(fridge, register2) == None):
                    writer.writerow([fridge.name, register1.ExclusiveShopName(fridge, register2)])






