class Player:
#====Блок инициализации====
    name = ""#Имя игрока
    cash = 0#Деньги игрока

    #Сертификаты на торговлю
    certs = {
        "Cars": False,
        "HomeAppliances": False,
        "Machines": False,
        "Furniture": False,
        "Hupermarket": False
    }

    #Размер кридита и текущий процент по кредиту
    credit = 0
    percentCredit = 0
    creditPeriod = 0

    #ресурсы игрока
    resources = {
        "Material": 0,
        "Cars": 0,
        "HomeAppliances": 0,
        "Machines": 0,
        "Furniture": 0
    }

#====Конструктор класса===
#====Создание игрока====
    def __init__(self, name):
        self.name = name
        self.cash = 25000

#====Операции с собственностью====
    def purchaseCompany(self, company):
        if (companies.get(company).getOwner() != None):
            print("This company has an owner")
        else:
            if (companies.get(company).getPurchase()>self.cash):
                print("Not enough money")
            else:
                self.cash -= companies.get(company).getPurchase()
                companies.get(company).setOwner(self.name)
                print("You bought the company")

    def saleCompany(self, company):
        if (companies.get(company).getOwner()==self.name):
            companies.get(company).resetOwner()
            self.cash += companies.get(company).getSale()
        else:
            print("This company does not belong to you")

#====Операции с кредитами====
    def takeCredit(self, credit):
        if (self.credit != 0):
            print("Denied! You have not repaid your current credit")
        else:
            self.credit = credit
            self.creditPeriod = 20

    def creditContril(self):
        if(self.credit != 0):
            self.creditPeriod -= 1
            self.percentCredit += self.credit * 0.1
            if (self.percentCredit == 0):
                print("You're bankrupt!")

    def repayCredit(self):
        if ((self.credit + self.percentCredit) <= self.cash):
            self.cash -= self.credit + self.percentCredit
            self.credit = 0
            self.percentCredit = 0
            self.creditPeriod = 0
        else:
            print("You don't have enough money")

    def repayPercentCredit(self):
        if(self.percentCredit <= self.cash):
            self.cash -= self.percentCredit
            self.percentCredit = 0
        else:
            print("You don't have enough money")

#====Операции с лицензиями====

    def purchCert(self,cert):
        if (cert=="Hypermarket"):
            if (self.cash < 50000):
                print("Not enough money")
                return 0
            self.cash -= 50000
            self.certs.update({cert,True})
        else:
            if (self.cash < 10000):
                print("Not enough money")
                return 0
            self.cash -= 10000
            self.certs.update({cert,True})

    def saleCert(self,cert):
        if (cert=="Hypermarket"):
            if(self.certs.get(cert)==False):
                print("You do not have this certificate")
                return 0
            self.certs.update({cert:False})
            self.cash += 50000
        else:
            if (self.certs.get(cert)==False):
                print("You do not have this certificate")
                return 0
            self.certs.update({cert:False})
            self.cash += 10000

    def reserCerts(self):
        for c in list(self.certs):
            self.certs.update({c:False})

    def getCert(self, cert):
        return self.certs.get(cert)
#====Операциями с ресурсами игрока====
    def getName(self):
        return self.name

    def getCash(self):
        return self.cash

    def addCash(self, cash):
        self.cash += cash

    def getResource(self, resource):
        return self.resources.get(resource)

    def addResources(self, resource, count):
        addRes = self.resources.get(resource) + count
        self.resources.update({resource: addRes})

#====Добыча сырья====
    def productionOfMaterials(self, company):
        if (companies.get(company).getType() != "Materials"):
            print("This company does not produce materials")
            return 0
        if (companies.get(company).getOwner()!=self.name):
            print("This company does not belong to you")
            return 0
        self.addResources("Materials", companies.get(company).getProduction())

#====Производство товара====
    def productionOfProduct(self, company, product):
        if (companies.get(company).getOwner() != self.name):
            print("This company does not belong to you")
            return 0
        if (companies.get(company).getType() != "Product"):
            print("This company does not produce product")
            return 0
        if (self.resources.get("Material") == 0):
            print("No materials available")
            return 0
        if (self.resources.get("Material") <= companies.get(company).getProduction()):
            self.addResources(product,self.resources.get("Material"))
            self.resources.update({"Material":0})
        else:
            self.addResources(product,companies.get(company).getProduction())
            self.addResources("Materials",-(companies.get(company).getProduction()))
#====Реализация товара====
    def saleOfProduct(self,company):#===>Продажа в гипермаркете
        print("Sale in Hypermarket")
        if (companies.get(company).getOwner() != self.name):
            print("This company does not belong to you")
            return 0
        if (companies.get(company).getType() != "Hypermarket"):
            print("This company do not realization product")
            return 0
        if (self.certs.get("Hypermarket") != True):
            print("You don't have a license")
            return 0
        allProduct = {"Cars":0, "HomeAppliances":0, "Machines":0, "Furniture":0}
        capProduct = companies.get(company).getProduction()
        sumProduct = 0

        for w in ["Cars", "HomeAppliances", "Machines", "Furniture"]:
            prod = int(input(w))
            allProduct.update({w:prod})
            if(self.resources.get(w) < allProduct.get(w)):
                allProduct.update({w:self.resources.get(w)})
            sumProduct += allProduct.get(w)
            if (sumProduct > capProduct):
                allProduct.update({w:(allProduct.get(w)-(sumProduct-capProduct))})
                break

        if (allProduct == 0):
            print("You don't have prodoct")
            return 0

        for b in ["Cars", "HomeAppliances", "Machines", "Furniture"]:
            self.addCash(allProduct.get(b))
            self.addResources(b, -(allProduct.get(b)))

    def saleOfProduct(self,company, product):#===>Продажа в рознице
        print("Sale in shop")
        if (companies.get(company).getOwner() != self.name):
            print("This company does not belong to you")
            return 0
        if (companies.get(company).getType() != product):
            print("This company do not realization product")
            return 0
        if (self.certs.get(product) != True):
            print("You don't have a license")
            return 0
        if (self.resources.get(product) == 0):
            print("You do not have this product")
            return 0
        saleProduct = int(input(product))
        if (saleProduct > companies.get(company).getProduction()):
            saleProduct = companies.get(company).getProduction()
        if (saleProduct > self.resources.get(product)):
            saleProduct = self.resources.get(product)
        self.addCash(saleProduct)
        self.addResources(product, -(saleProduct))

    def saleOfProduct(self):#===>Продажа на бирже
        print("Sale in birse")
        allProduct = {"Cars": 0, "HomeAppliances": 0, "Machines": 0, "Furniture": 0}
        capProduct = companies.get(company).getProduction()
        sumProduct = 0

        for w in ["Cars", "HomeAppliances", "Machines", "Furniture"]:
            prod = int(input(w))
            allProduct.update({w: prod})
            if (self.resources.get(w) < allProduct.get(w)):
                allProduct.update({w: self.resources.get(w)})
            rest = allProduct.get(w) % 10000
            allProduct.update({w: (allProduct.get(w) - rest)})
            sumProduct += allProduct.get(w)
            if (sumProduct > capProduct):
                allProduct.update({w: (allProduct.get(w) - (sumProduct - capProduct))})
                break

        if (allProduct == 0):
            print("You don't have prodoct")
            return 0

        for b in ["Cars", "HomeAppliances", "Machines", "Furniture"]:
            self.addCash(allProduct.get(b)/2)
            self.addResources(b, -(allProduct.get(b)))

# ====Трейд с другими игроками====

    def tradeSaleProduct(self, playerTrade, typeProduct):#===>Продать ресурс другому игроку
        if (self.resources.get(typeProduct) == 0):
            print("You don't have prodoct")
            return 0
        product = int(input(typeProduct))
        if (product > self.resources.get(typeProduct)):
            product = self.resources.get(typeProduct)
        price = int(input("Price"))
        if (price > players.get(playerTrade).getCash()):
            price = players.get(playerTrade).getCash()
        consent = input("The trader agrees to the deal? Y/N")
        if (consent == "N"):
            print("The trader refused the deal")
            return 0
        self.addResources(typeProduct, -(product))
        players.get(playerTrade).addResources(typeProduct,product)
        players.get(playerTrade).addCash(-price)
        self.addCash(price)

    def tradePurchProduct(self, playerTrade, typeProduct):#===>Купить ресурс у другого игрока
        if (self.cash == 0):
            print("'You have no money")
            return 0
        product = int(input(typeProduct))
        if (product > players.get(playerTrade).getResource(typeProduct)):
            product = players.get(playerTrade).getResource(typeProduct)
        price = int(input("Price"))
        if (price > self.cash):
            price = self.cash
        consent = input("The trader agrees to the deal? Y/N")
        if (consent == "N"):
            print("The trader refused the deal")
            return 0
        players.get(playerTrade).addResources(typeProduct, -product)
        self.addResources(typeProduct, product)
        self.addCash(-price)
        players.get(playerTrade).addCash(price)


    def tradeSaleCompany(self, playerTrade, company):#===>Продать собственность другому игроку
        if (companies.get(company).getOwner() != self.name):
            print("This company is not yours")
            return 0
        if (players.get(playerTrade).getCash() == 0):
            print("The trader has no money")
        price = int(input("Price"))
        if (price > players.get(playerTrade).getCash()):
            price = players.get(playerTrade).getCash()
        consent = input("The trader agrees to the deal? Y/N")
        if (consent == "N"):
            print("The trader refused the deal")
            return 0
        companies.get(company).setOwner(playerTrade)
        players.get(playerTrade).addCash(-price)
        self.addCash(price)

    def tradePurchCompany(self, playerTrade, company):#===>Купить собственность у другого игрока
        if (companies.get(company).getOwner() != players.get(playerTrade).getName()):
            print("This company is not owned by the trader")
            return 0
        if (self.cash == 0):
            print("You have no money")
            return 0
        price = int(input("Price"))
        if (price > self.cash):
            price = self.cash
        consent = input("The trader agrees to the deal? Y/N")
        if (consent == "N"):
            print("The trader refused the deal")
            return 0
        companies.get(company).setOwner(self.name)
        self.addCash(-price)
        players.get(playerTrade).addCash(price)

    def stopCourse(self):
        Event.nextCircle()
        return True
class Company:
    cName = ""
    cType = ""
    cNumber = 0
    cPurchase = 0
    cSale = 0
    cProduction = 0
    cOwner = 0

    def __init__(self, cName, cType, cNumber, cPurchase, cSale, cProduction):
        self.cName = cName
        self.cType = cType
        self.cNumber = cNumber
        self.cPurchase = cPurchase
        self.cSale = cSale
        self.cProduction = cProduction
        self.cOwner = None

    def getType(self):
        return self.cType

    def getPurchase(self):
        return self.cPurchase

    def getSale(self):
        return self.cSale

    def getOwner(self):
        return self.cOwner

    def setOwner(self, playerName):
        self.cOwner = playerName

    def resetOwner(self):
        self.cOwner = None

    def getProduction(self):
        return self.cProduction

    def getName(self):
        return self.cNamee

class Event:
    game = ""
    course = 0
    circle = 0
    # playersCount = len(players)
    # curretPlayer = ""
    playersCount = 6
    productionOfMaterials = True
    productionOfMaterialsCourse = 0
    productionOfMaterialsCircle = 0
    productionOfProduct = True
    productionOfProductCourse = 0
    productionOfProductCircle = 0

    def __init__(self, game):
        self.game = game

    def nextPlayer(self):
        self.course += 1
        if (self.course >= self.playersCount):
            self.nextCircle()
            self.course = 0

    def nextCircle(self):
        self.circle += 1

    def natureProtectionControl(self):
        if (self.productionOfMaterials == False):
            if (self.productionOfMaterialsCircle == self.circle+1 and self.productionOfMaterialsCourse == self.course+1):
                self.productionOfMaterials = True
        else:
            print("Extraction of materials is illegal")

    def natureProtection(self):
        self.productionOfMaterials = False
        self.productionOfMaterialsCircle = self.circle
        self.productionOfMaterialsCourse = self.course

    def crisisOfOverproduction(self):
        if (self.productionOfProduct == False):
            if (
                    self.productionOfProductCircle == self.circle + 1 and self.productionOfProductCourse == self.course + 1):
                self.productionOfProduct = True
        else:
            print("Production is illegal")

    def crisisOfOverproductionControl(self):
        self.productionOfProduct = False
        self.productionOfProductCircle = self.circle
        self.productionOfProductCourse = self.course

    def certsCommittee(self):
        for p in list(players):
            players.get(p).reserCerts()

    def taxInspection(self):
        for p in list(players):
            tax = -(players.get(p).getCash()*0.1)
            players.get(p).addCash(tax)

    def getCurretPlayer(self, numberPlayer):
        playersName = []
        for p in list(players):
            playersName.append(players.get(p).getName())
        return playersName[numberPlayer]


companies = {}

for companyName in ["Materials", "HomeAppliances", "Cars", "Machines", "Furniture", "shopHomeAppliances", "shopCars", "shopMachines", "shopFurniture","Hypermarket"]:
    if companyName == "Materials":
        rangeNumber = [1,2,3,4,5,6,7,8,9,10,11,12]
        companyType = "Materials"
        # print(companyType)
    if companyName == "HomeAppliances" or companyName == "Cars" or companyName == "Machines" or companyName == "Furniture":
        rangeNumber = [1,2,3,4,5]
        companyType = "Product"
        # print(companyType)
    if companyName == "shopHomeAppliances" or companyName == "shopCars" or companyName == "shopMachines" or companyName == "shopFurniture" or companyName == "Hypermarket":
        rangeNumber = [1,2,3,4]
        companyType = "Shop"
        # print(companyType)
    for companyNumber in rangeNumber:
        companyPurch = 15000 * companyNumber
        companySale = companyPurch * companyNumber - 5000 * companyNumber
        companyProd = 5000 * companyNumber
        companyKey = companyName + str(companyNumber)
        company = Company(companyName, companyType, companyNumber, companyPurch, companySale, companyProd)
        # print(company.getType())
        companyKey = companyName + str(companyNumber)
        # print(companyKey)
        if (companies == None):
            companies = dict.fromkeys([companyKey],company)
        else:
            companies[companyKey] = company
        # print(companies.values())

players = {}
for p in ["Ivan", "Petay", "Igor", "Masha", "Katay", "Natasha"]:
    player = Player(p)
    players[p] = player

