import pygame
import sys
import json
import Main

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((1350, 670))

white = [255, 255, 255]
black = [0,0,0]
darkgreen = [0, 120, 0]
darkred = [120, 0, 0]
boxes = dict()
with open("blocks.json","r") as readFile:
    data = json.load(readFile)
#=====Параметры нижней панели====
X_TOOLBAR = 0
Y_TOOLBAT = 601
W_TOOLBAR = 1350
H_TOOLBAR = 70
COLOR_TOOLBAT = [100,100,50]
#=====Параметры меню======
X_MENU = 1001
Y_MENU = 0
W_MENU = 350
H_MENU = 670
COLOR_MENU = [100,50,100]


pygame.display.update()
COUNT_W=1000/10
COUNT_H=600/10

gameSession = Main.Event("Test")

f = pygame.font.SysFont("calibri", 16)
listActionBlock = []

# course = gameSession.course
# circle = gameSession.circle
# curretPlayer = gameSession.getCurretPlayer(course)

class StatusBar():
    status = 0
    action = "default"
    def __init__(self):
        pass

# Status = StatusBar
class Box:
    x = 0
    y = 0
    w = 0
    h = 0
    blockID = ""
    name = ""
    blockType = 0
    resources = ""
    pricePurchase = 0
    priceSale = 0
    production = 0
    color = white
    lockPlayer = None


    # print(lockPlayer)
    def __init__(self,x,y,w,h,blockID, name,color, resources, pricePurchase, priceSale, production, blockType):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.blockID = blockID
        self.name = name
        self.resources = resources
        self.color = color
        self.pricePurchase = pricePurchase
        self.priceSale= priceSale
        self.production = production
        self.blockType = blockType
        self.lockPlayer = dict()

    def drawBox(self):
        pygame.draw.rect(sc, (self.color), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(sc, (black), (self.x, self.y, self.w, self.h), 2)

        if (self.blockType == 1 or self.blockType == 2 or self.blockType == 3):
            if (Main.companies.get(self.blockID).getOwner() == gameSession.getCurretPlayer(gameSession.course)):
                pygame.draw.rect(sc, (darkgreen), (self.x, self.y, self.w, self.h), 4)
            elif(Main.companies.get(self.blockID).getOwner() != gameSession.getCurretPlayer(gameSession.course) and Main.companies.get(self.blockID).getOwner() != "default"):
                pygame.draw.rect(sc, (darkred), (self.x, self.y, self.w, self.h), 4)
        if (self.blockType == 4 and self.blockID != "Trade"):
            if (self.lockPlayer.get(gameSession.getCurretPlayer(gameSession.course)) != 0):
                pygame.draw.rect(sc, (darkred), (self.x, self.y, self.w, self.h), 6)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getW(self):
        return self.w

    def getH(self):
        return self.h

    def getName(self):
        return self.name

    def getPricePurchase(self):
        return self.pricePurchase

    def getPriceSale(self):
        return self.priceSale

    def getProduction(self):
        return self.production

    def getBlockId(self):
        return self.blockID

    def getBlockType(self):
        return self.blockType

    def getResources(self):
        return self.resources

    def creatLockControl(self):
        for p in list(Main.players):
            self.lockPlayer.update({p:0})

    def lockControll(self, player):
        # print(self.lockPlayer)
        # print(self.blockID)
        if (self.lockPlayer.get(player) == 0):
            # self.lockPlayer.update({player:2})
            boxes.get(self.blockID).lockPlayer.update({player:2})
            # print("OK")
            return "OK"
        else:
            return "NO"

    def lockControllDel(self, player):
        for b in listActionBlock:
            if(boxes.get(b).lockPlayer.get(player) != 0):
                # print(b)
                curretLockStatus = boxes.get(b).lockPlayer.get(player)
                boxes.get(b).lockPlayer.update({player: (curretLockStatus - 1)})
                # print("For Block: " + str(boxes.get(b).getBlockId()) + " unlock process for player: " + gameSession.getCurretPlayer(gameSession.course))
                # print("Lock status for this block: " + str(boxes.get(b).lockPlayer))

#====Создание блоков====

def createListActionBlock():
    for b in list(boxes):
        if (boxes.get(b).getBlockType() == 4 and boxes.get(b).getBlockId() != "Trade"):
            listActionBlock.append(boxes.get(b).getBlockId())

def unlocerBlocksForPlayer(player):
    for b in listActionBlock:
        boxes.get(b).lockControllDel(player)

def createBlocks():

#=====Создание полей действий=====
    block = Box(1 * COUNT_W, 0 * COUNT_H, COUNT_W * 2, COUNT_H, "ProductionOfMaterials","Добыча материалов", [0, 255, 255],  "", "", "", "", 4)
    block.creatLockControl()
    boxes.update({("ProductionOfMaterials"): block})
    block = Box(5 * COUNT_W, 0 * COUNT_H, COUNT_W * 2, COUNT_H, "ProductionOfProduct","Производство товара", [0, 255, 255], "", "", "", "", 4)
    block.creatLockControl()
    boxes.update({("ProductionOfProduct"): block})
    block = Box(9 * COUNT_W, 0 * COUNT_H, COUNT_W, COUNT_H * 2, "Ecology", "Защита природы", [0, 255, 255], "", "", "", "", 4)
    block.creatLockControl()
    boxes.update({("Ecology"): block})
    block = Box(9 * COUNT_W, 4 * COUNT_H, COUNT_W, COUNT_H * 2, "Crysis", "Кризис перепроизводства", [0, 255, 255], "", "", "", "", 4)
    block.creatLockControl()
    boxes.update({("Crysis"): block})
    block = Box(9 * COUNT_W, 7 * COUNT_H, COUNT_W, COUNT_H * 2, "Bank", "Банк", [0, 255, 255], "", "", "", "", 4)
    block.creatLockControl()
    boxes.update({("Bank"): block})
    block = Box(0 * COUNT_W, 1 * COUNT_H, COUNT_W, COUNT_H * 2, "Birsa", "Биржа", [0, 255, 255], "", "", "", "", 4)
    block.creatLockControl()
    boxes.update({("Birsa"): block})
    block = Box(0 * COUNT_W, 4 * COUNT_H, COUNT_W, COUNT_H * 2, "Committe", "Лицензионный коммитет", [0, 255, 255], "", "", "", "", 4)
    block.creatLockControl()
    boxes.update({("Committe"): block})
    block = Box(0 * COUNT_W, 8 * COUNT_H, COUNT_W, COUNT_H * 2, "ShopOfProduct", "Сбыт", [0, 255, 255], "", "", "", "", 4)
    block.creatLockControl()
    boxes.update({("ShopOfProduct"): block})
    block = Box(2 * COUNT_W, 9 * COUNT_H, COUNT_W * 2, COUNT_H, "Shop", "Рынок", [0, 255, 255], "", "", "", "", 4)
    block.creatLockControl()
    # print(block.lockPlayer)
    boxes.update({("Shop"): block})
    block = Box(6 * COUNT_W, 9 * COUNT_H, COUNT_W * 2, COUNT_H, "Nalog", "Налоговая инспекция", [0, 255, 255], "", "", "", "", 4)
    block.creatLockControl()
    boxes.update({("Nalog"): block})
    block = Box(4 * COUNT_W, 4 * COUNT_H, COUNT_W * 2, COUNT_H * 2, "Trade", "Трейд", [0, 255, 255], "", "", "", "", 4)
    # block.creatLockControl()
    boxes.update({("Trade"): block})
#=====Создание пустых блоков=====
    block = Box(0 * COUNT_W, 0 * COUNT_H, COUNT_W, COUNT_H, "empty0", "", [20, 20, 20], "", "", "", "", 10)
    boxes.update({("empty0"): block})
    block = Box(3 * COUNT_W, 0 * COUNT_H, COUNT_W * 2, COUNT_H, "empty1", "", [20, 20, 20], "", "", "", "", 10)
    boxes.update({("empty1"): block})
    block = Box(7 * COUNT_W, 0 * COUNT_H, COUNT_W * 2, COUNT_H, "empty2", "", [20, 20, 20], "", "", "", "", 10)
    boxes.update({("empty2"): block})
    block = Box(1 * COUNT_W, 9 * COUNT_H, COUNT_W, COUNT_H, "empty3", "", [20, 20, 20], "", "", "", "", 10)
    boxes.update({("empty3"): block})
    block = Box(4 * COUNT_W, 9 * COUNT_H, COUNT_W * 2, COUNT_H, "empty4", "", [20, 20, 20], "", "", "", "", 10)
    boxes.update({("empty4"): block})
    block = Box(8 * COUNT_W, 9 * COUNT_H, COUNT_W * 2, COUNT_H, "empty5", "", [20, 20, 20], "", "", "", "", 10)
    boxes.update({("empty5"): block})
    block = Box(0 * COUNT_W, 3 * COUNT_H, COUNT_W, COUNT_H, "empty6", "", [20, 20, 20], "", "", "", "", 10)
    boxes.update({("empty6"): block})
    block = Box(0 * COUNT_W, 6 * COUNT_H, COUNT_W, COUNT_H * 2, "empty7", "", [20, 20, 20], "", "", "", "", 10)
    boxes.update({("empty7"): block})
    block = Box(9 * COUNT_W, 2 * COUNT_H, COUNT_W, COUNT_H * 2, "empty8", "", [20, 20, 20], "", "", "", "", 10)
    boxes.update({("empty8"): block})
    block = Box(9 * COUNT_W, 6 * COUNT_H, COUNT_W, COUNT_H, "empty9", "", [20, 20, 20], "", "", "", "", 10)
    boxes.update({("empty9"): block})
    block = Box(1005, 300, 75, 25, "Cancel", "Отмена", [225,225,255], "", "", "", "", 0)
    boxes.update({("Cancel"): block})
    block = Box(1005, 330, 75, 25, "Purchase", "Купить", [225,225,255], "", "", "", "", 5)
    boxes.update({("Purchase"): block})
    block = Box(1005, 360, 75, 25, "Sale", "Продать", [225,225,255], "", "", "", "", 5)
    boxes.update({("Sale"): block})
    block = Box(1105, 300, 75, 25, "count1000", "1000", [225,225,255], "", "", "", "", 6)
    boxes.update({("count1000"): block})
    block = Box(1105, 330, 75, 25, "count5000", "5000", [225,225,255], "", "", "", "", 6)
    boxes.update({("count5000"): block})
    block = Box(1105, 360, 75, 25, "count10000", "10000", [225,225,255], "", "", "", "", 6)
    boxes.update({("count10000"): block})
    block = Box(1105, 390, 75, 25, "count20000", "20000", [225,225,255], "", "", "", "", 6)
    boxes.update({("count20000"): block})
    block = Box(1185, 300, 75, 25, "count50000", "50000", [225,225,255], "", "", "", "", 6)
    boxes.update({("count50000"): block})
    block = Box(1185, 330, 75, 25, "count100000", "100000", [225,225,255], "", "", "", "", 6)
    boxes.update({("count100000"): block})
    block = Box(1185, 360, 75, 25, "count200000", "200000", [225,225,255], "", "", "", "", 6)
    boxes.update({("count200000"): block})
    block = Box(1185, 390, 75, 25, "count500000", "500000", [225,225,255], "", "", "", "", 6)
    boxes.update({("count500000"): block})

    #=====Создание полей предприятий=====
    blocksName = ["Material", "HomeAppliances", "Cars", "Furniture", "Machines", "shopFurniture", "shopCars", "shopHomeAppliances", "shopMachines", "Hupermarket"]
    def createBox(boxName, number):
        id = boxName + str(number)
        name = boxName
        # number = number
        # print(name)
        x = data[id]["x_coordinate"]
        y = data[id]["y_coordonate"]
        color = data[id]["color"]
        blockType = data[id]["type"]
        resources = data[id]["resources"]
        pricePurchase = data[id]["pricePurchase"]
        priceSale = data[id]["priceSale"]
        production = data[id]["production"]
        company = Main.Company(name, blockType, number, pricePurchase, priceSale, production)
        gameSession.createCompany(id, company)
        box = Box(x * COUNT_W, y * COUNT_H, COUNT_W, COUNT_H, id, name, color, resources, pricePurchase, priceSale, production, blockType)
        if (id == "Hupermarket0"):
            box = Box(x * COUNT_W, y * COUNT_H, COUNT_W, COUNT_H * 3, id, name, color, resources, pricePurchase, priceSale, production, blockType)
        if (id == "Hupermarket1"):
            box = Box(x * COUNT_W, y * COUNT_H, COUNT_W * 3, COUNT_H, id, name, color, resources, pricePurchase, priceSale, production, blockType)
        if (id == "Hupermarket2"):
            box = Box(x * COUNT_W, y * COUNT_H, COUNT_W *3, COUNT_H, id, name, color, resources, pricePurchase, priceSale, production, blockType)
        if (id == "Hupermarket3"):
            box = Box(x * COUNT_W, y * COUNT_H, COUNT_W, COUNT_H * 3, id, name, color, resources, pricePurchase, priceSale, production, blockType)
        boxes.update({id:box})


    for b in blocksName:
        if (b == "Material"):
            for q in range(12):
                createBox(b, q)
        if (b == "HomeAppliances"):
            for q in range(5):
                createBox(b, q)
        if (b == "Cars"):
            for q in range(5):
                createBox(b, q)
        if (b == "Furniture"):
            for q in range(5):
                createBox(b, q)
        if (b == "Machines"):
            for q in range(5):
                createBox(b, q)
        if (b == "shopFurniture"):
            for q in range(4):
                createBox(b, q)
        if (b == "shopCars"):
            for q in range(4):
                createBox(b, q)
        if (b == "shopHomeAppliances"):
            for q in range(4):
                createBox(b, q)
        if (b == "shopMachines"):
            for q in range(4):
                createBox(b, q)
        if (b == "Hupermarket"):
            for q in range(4):
                createBox(b, q)

def searchBox(searchedX,searchedY):
    # if (searchedX >= 0 and searchedX <= 1000 and searchedY >= 0 and searchedY <= 600):
    for box in list(boxes):
        x = boxes.get(box).getX()
        y = boxes.get(box).getY()
        w = boxes.get(box).getW() + x
        h = boxes.get(box).getH() + y
        # print("Box searching: " + str(box))
        if (searchedX >= x and searchedX <= w and searchedY >= y and searchedY <= h):
            return box

def eventControllAction(blockId):
    blockType = boxes.get(blockId).getBlockType()
    curretPlayer = gameSession.getCurretPlayer(gameSession.course)
    lockStatus = boxes.get(blockId).lockPlayer
    lockStatusForCurretPlayer = lockStatus.get(curretPlayer)
    # print("blockId: " + str(blockId))
    # print("blockType: " + str(blockType))
    # print("curretPlayer: " + str(curretPlayer))
    # print("lockStatus: " + str(lockStatus))
    # print("lockStatusForCurretPlayer: " + str(lockStatusForCurretPlayer))
    # print("eventControllAction")
    if (lockStatusForCurretPlayer == 0):
        if (blockId == "Birsa"):
            # Main.players.get(curretPlayer).saleOfProduct()
            pass
        if (blockId == "Committe"):
            gameSession.certsCommittee()
            StatusBar.status = 0
            StatusBar.action = "default"
            boxes.get("Committe").lockControll(gameSession.getCurretPlayer(gameSession.course))
        if (blockId == "ShopOfProduct"):
            pass
        if (blockId == "Shop"):
            StatusBar.status = 1
            StatusBar.action = "purchAndSale"
            # print(StatusBar.status)
            # print(StatusBar.action)
            pass
        if (blockId == "Nalog"):
            gameSession.taxInspection()
            StatusBar.status = 0
            StatusBar.action = "default"
            boxes.get("Nalog").lockControll(gameSession.getCurretPlayer(gameSession.course))
        if (blockId == "Bank"):
            pass
        if (blockId == "Crysis"):
            gameSession.crisisOfOverproduction()
            StatusBar.status = 0
            StatusBar.action = "default"
            boxes.get("Crysis").lockControll(gameSession.getCurretPlayer(gameSession.course))
        if (blockId == "Ecology"):
            gameSession.natureProtection()
            StatusBar.status = 0
            StatusBar.action = "default"
            boxes.get("Ecology").lockControll(gameSession.getCurretPlayer(gameSession.course))
        if (blockId == "ProductionOfProduct" and gameSession.productionOfProduct == True):
            StatusBar.status = 1
            StatusBar.action = "ProductionOfProduct"
        if (blockId == "ProductionOfMaterials" and gameSession.productionOfMaterials == True):
            StatusBar.status = 1
            StatusBar.action = "ProductionOfMaterials"
        if (blockId == "Trade"):
            # boxes.get("Shop").lockControll(gameSession.getCurretPlayer(gameSession.course))
            # print("Test")
            pass

def eventController(blockId):
    if (blockId == None): #Ничего не происходит. Не нажата кнопка
        return 0
    if (blockId == "Cancel"):#Отмена действия. Возврат в статус 0
        StatusBar.status = 0
        StatusBar.action = "default"
    blockType = boxes.get(blockId).getBlockType()
    if (blockType == 10): #Конец хода. Переход в статус 0. Переход к другому игроку
        # print("event control")
        StatusBar.status = 0
        boxes.get(blockId).lockControllDel(gameSession.getCurretPlayer(gameSession.course))
        gameSession.nextPlayer()
        gameSession.crisisOfOverproductionControl()
        gameSession.natureProtectionControl()
    if (blockType == 4 and StatusBar.status == 0):
        eventControllAction(blockId)

    if (StatusBar.status == 1 and blockType == 5 and StatusBar.action == "purchAndSale"):#Выбор Купить/Продать
        if (blockId == "Purchase"):
            StatusBar.action = "Purchase"
        if (blockId == "Sale"):
            StatusBar.action = "Sale"

    if (StatusBar.status == 1 and (blockType == 1 or blockType == 2 or blockType == 3) and (StatusBar.action == "Purchase" or StatusBar.action == "Sale")):#Покупка/Продажа собственности
        if (StatusBar.action == "Purchase"):
            result = Main.players.get(gameSession.getCurretPlayer(gameSession.course)).purchaseCompany(blockId)
            if (result == "OK"):
                StatusBar.status = 0
                StatusBar.action = "default"
                boxes.get("Shop").lockControll(gameSession.getCurretPlayer(gameSession.course))
        if (StatusBar.action == "Sale"):
            result = Main.players.get(gameSession.getCurretPlayer(gameSession.course)).saleCompany(blockId)
            if (result == "OK"):
                StatusBar.status = 0
                StatusBar.action = "default"
                boxes.get("Shop").lockControll(gameSession.getCurretPlayer(gameSession.course))
    if (StatusBar.status == 1 and blockType == 1 and StatusBar.action == "ProductionOfMaterials"): #Добыча материалов
        Main.companies.get(blockId).getType()
        # print("type company: " + str(Main.companies.get(blockId).getType()))
        # print("type block: " + str(boxes.get(blockId).getBlockType()))
        result = Main.players.get(gameSession.getCurretPlayer(gameSession.course)).productionOfMaterials(blockId)
        if (result == "OK"):
            StatusBar.status = 0
            StatusBar.action = "default"
            boxes.get("ProductionOfMaterials").lockControll(gameSession.getCurretPlayer(gameSession.course))
    if (StatusBar.status == 1 and StatusBar.action == "ProductionOfProduct" and blockType == 2):#Производство Товара
        result = Main.players.get(gameSession.getCurretPlayer(gameSession.course)).productionOfProduct(blockId, boxes.get(blockId).getResources())
        if (result == "OK"):
            StatusBar.status = 0
            StatusBar.action = "default"
            boxes.get("ProductionOfProduct").lockControll(gameSession.getCurretPlayer(gameSession.course))
    if (blockType == 6):
        gameSession.
def writePlayerData():
    curretPlayer = gameSession.getCurretPlayer(gameSession.course)
    count = gameSession.writingCount
    textPlayer = f.render("Игрок: " + curretPlayer, 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 15))
    textPlayer = f.render("Деньги: " + str(Main.players.get(curretPlayer).getCash()), 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 30))
    textPlayer = f.render("Материалы: " + str(Main.players.get(curretPlayer).getResource("Material")), 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 45))
    textPlayer = f.render("Автомобили: " + str(Main.players.get(curretPlayer).getResource("Cars")), 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 60))
    textPlayer = f.render("Бытовая техника: " + str(Main.players.get(curretPlayer).getResource("HomeAppliances")), 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 75))
    textPlayer = f.render("Станки: " + str(Main.players.get(curretPlayer).getResource("Machines")), 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 90))
    textPlayer = f.render("Мебель: " + str(Main.players.get(curretPlayer).getResource("Furniture")), 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 105))
    textPlayer = f.render("Лицензия на автомобилей: " + str(Main.players.get(curretPlayer).getCert("Cars")), 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 120))
    textPlayer = f.render("Лицензия на бытовой техники: " + str(Main.players.get(curretPlayer).getCert("HomeAppliances")), 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 135))
    textPlayer = f.render("Лицензия на станков: " + str(Main.players.get(curretPlayer).getCert("Machines")), 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 150))
    textPlayer = f.render("Лицензия на мебели: " + str(Main.players.get(curretPlayer).getCert("Furniture")), 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 165))
    textPlayer = f.render("Лицензия на гипермаркет : " + str(Main.players.get(curretPlayer).getCert("Hupermarket")), 1, (0, 0, 0))
    sc.blit(textPlayer, (1050, 180))
    textPlayer = f.render("Колиество : " + str(count), 1, (0, 0, 0))
    sc.blit(textPlayer, (1105, 420))

def writeStatus():
    curretPlayer = gameSession.getCurretPlayer(gameSession.course)
    textPlayer = f.render("Игрок: " + curretPlayer, 1, (0, 0, 0))
    sc.blit(textPlayer, (20, 630))
    textPlayer = f.render("Круг: " + str(gameSession.circle), 1, (0, 0, 0))
    sc.blit(textPlayer, (130, 630))
    textPlayer = f.render("Status: " + str(StatusBar.status), 1, (0, 0, 0))
    sc.blit(textPlayer, (20, 645))
    textPlayer = f.render("Action: " + str(StatusBar.action), 1, (0, 0, 0))
    sc.blit(textPlayer, (130, 645))
    textPlayer = f.render("Ecology: " + str(gameSession.productionOfMaterials), 1, (0, 0, 0))
    sc.blit(textPlayer, (250, 645))
    textPlayer = f.render("Crisis: " + str(gameSession.productionOfProduct), 1, (0, 0, 0))
    sc.blit(textPlayer, (250, 630))

def drawGameField():
    for block in list(boxes):
        boxes.get(block).drawBox()
        text = f.render(boxes.get(block).getName() , 1, (0, 0, 0))
        sc.blit(text, (boxes.get(block).getX() + 10, boxes.get(block).getY() + 4))
        text = f.render(str(boxes.get(block).getPricePurchase()), 1, (0, 0, 0))
        sc.blit(text, (boxes.get(block).getX() + 10, boxes.get(block).getY() + 17))
        text = f.render(str(boxes.get(block).getPriceSale()), 1, (0, 0, 0))
        sc.blit(text, (boxes.get(block).getX() + 10, boxes.get(block).getY() + 28))
        text = f.render(str(boxes.get(block).getProduction()), 1, (0, 0, 0))
        sc.blit(text, (boxes.get(block).getX() + 10, boxes.get(block).getY() + 39))

createBlocks()
createListActionBlock()
# print(Main.companies)
while 1:

    sc.fill(white)
    clock.tick(60)
    # for i in range(10):
    #     for j in range(10):
    #         pygame.draw.rect(sc, (0, 0, 0), ((120*j), (60*i), 120, 60), 1)
    pygame.draw.rect(sc, COLOR_TOOLBAT, (X_TOOLBAR, Y_TOOLBAT, W_TOOLBAR, H_TOOLBAR))
    pygame.draw.rect(sc, COLOR_MENU, (X_MENU, Y_MENU, W_MENU, H_MENU))

    # pygame.draw.text(text, (200,200))
    drawGameField()
    writePlayerData()
    writeStatus()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pygame.draw.circle(sc, [255,0,0], i.pos, 10)
                pygame.display.update()
                # print(i.pos)
                # print(i.pos[0])
                # print(i.pos[1])
                # print(searchBox(i.pos[0], i.pos[1]))
                eventController(searchBox(i.pos[0], i.pos[1]))
    pygame.display.update()
    pygame.time.delay(100)

