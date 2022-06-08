from Fridge import Fridge


class FridgesRegister:
    def __init__(self):
        self.__allFridges = list()
        self.__shop = ""
        self.__address = ""
        self.__phoneNumber = ""
        self.__ids = list()

    def PutShop(self, shop, address, phoneNumber):
        self.__shop = shop
        self.__address = address
        self.__phoneNumber = phoneNumber

    def GetShop(self):
        return self.__shop
    def GetAddress(self):
        return self.__address
    def getPhoneNumber(self):
        return self.__phoneNumber
    def FridgesRegister(self):
        self.__allFridges = list()

    def FridgesRegister(self, fridges):
        self.__allFridges = list()
        for fridge in fridges:
            self.__allFridges.Add(fridge)

    def Add (self, fridge: Fridge) -> FridgesRegister:
        self.__allFridges.append(fridge)

    def Contains (self, fridge) -> bool:
        if fridge in self.__allFridges:
            return True
        else:
            return False

    def FridgesCount(self):
        return len(self.__allFridges)

    def GetFridge (self, index: int) -> Fridge:
        return self.__allFridges[index]

    def HighestCost(self) -> float:
        cost = list()
        for fridge in self.__allFridges:
            if fridge.volume >= 80:
                p = fridge.price
                if not p in cost:
                    cost.append(p)


        return max(cost)

    def HighestManufacturerCost(self) -> float:
        cost = list()
        for fridge in self.__allFridges:
            p = fridge.price
            if not p in cost:
                cost.append(p)
        return max(cost)

    def FindExclusiveManufacturers(self, register: FridgesRegister) -> FridgesRegister:
        exclusiveManufacturers = FridgesRegister()
        for i in range(self.FridgesCount()):
            fridge1 = self.GetFridge(i)
            for j in range(register.FridgesCount()):
                fridge2 = register.GetFridge(j)
                if fridge1.name == fridge2.name:
                   break
                if j == register.FridgesCount() - 1:
                        if not exclusiveManufacturers.Contains(fridge1):
                            exclusiveManufacturers.Add(fridge1)
                            exclusiveManufacturers.__ids.append(fridge1.id)
                            #print(fridge1.id)

        for i in range(register.FridgesCount()):
            fridge2 = register.GetFridge(i)
            for j in range(self.FridgesCount()):
                fridge1 = self.GetFridge(j)
                if fridge1.name == fridge2.name:
                    break
                if j == self.FridgesCount() - 1:
                    if not exclusiveManufacturers.Contains(fridge2):
                        exclusiveManufacturers.Add(fridge2)
                        exclusiveManufacturers.__ids.append(fridge2.id)
                        #print(fridge1.id)

        return exclusiveManufacturers

    def ExclusiveShopName (self, fridge: Fridge, register2: FridgesRegister) -> str:
        for i in range(self.FridgesCount()):
            fridge1 = self.GetFridge(i)
            shop1 = str(self.GetShop())
            if fridge1.id == fridge.id:
                return shop1
        for i in range(register2.FridgesCount()):
            fridge1 = register2.GetFridge(i)
            shop2 = str(register2.GetShop())
            if fridge1.id == fridge.id:
                return shop2