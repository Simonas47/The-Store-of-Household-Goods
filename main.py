from InOutUtils import InOutUtils

fileName1 = '1Viskas_Buičiai.csv' # initial files
fileName2 = '1Viskas_Namams.csv'
fileName3 = 'Tik_Ten.csv'

f = InOutUtils()
fridges1 = f.ReadFridges(fileName1)
fridges2 = f.ReadFridges(fileName2)


f = InOutUtils()
f.PrintInitialData(fridges1, fridges2)

f.PrintMostExpensiveFridges(fridges1, fridges2)
f.PrintMostExpensiveManufacturer(fridges1)
f.PrintMostExpensiveManufacturer(fridges2)
f.PrintExclusiveManufacturers(fileName3, fridges1, fridges2)