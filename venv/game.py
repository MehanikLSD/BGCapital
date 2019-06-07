import pygame
import sys
import json
import Main

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((1350, 670))

white = [255, 255, 255]
black = [0,0,0]
boxes = {}
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


# course = gameSession.course
# circle = gameSession.circle
# curretPlayer = gameSession.getCurretPlayer(course)

class StatusBar():
    text = ""

    def __init__(self):
        pass
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
    blockType = 0
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

    def drawBox(self):
        pygame.draw.rect(sc, (self.color), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(sc, (black), (self.x, self.y, self.w, self.h), 2)

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
#====Создание блоков====
def createBlocks():

#=====Создание полей действий=====
    block = Box(1 * COUNT_W, 0 * COUNT_H, COUNT_W * 2, COUNT_H, "ProductionOfMaterials","Добыча материалов", [0, 255, 255],  "", "", "", "", 4)
    boxes.update({("ProductionOfMaterials"): block})
    block = Box(5 * COUNT_W, 0 * COUNT_H, COUNT_W * 2, COUNT_H, "ProductionOfProduct","Производство товара", [0, 255, 255], "", "", "", "", 4)
    boxes.update({("ProductionOfProduct"): block})
    block = Box(9 * COUNT_W, 0 * COUNT_H, COUNT_W, COUNT_H * 2, "Ecology", "Защита природы", [0, 255, 255], "", "", "", "", 4)
    boxes.update({("Ecology"): block})
    block = Box(9 * COUNT_W, 4 * COUNT_H, COUNT_W, COUNT_H * 2, "Crysis", "Кризис перепроизводства", [0, 255, 255], "", "", "", "", 4)
    boxes.update({("Crysis"): block})
    block = Box(9 * COUNT_W, 7 * COUNT_H, COUNT_W, COUNT_H * 2, "Bank", "Банк", [0, 255, 255], "", "", "", "", 4)
    boxes.update({("Bank"): block})
    block = Box(0 * COUNT_W, 1 * COUNT_H, COUNT_W, COUNT_H * 2, "Birsa", "Биржа", [0, 255, 255], "", "", "", "", 4)
    boxes.update({("Birsa"): block})
    block = Box(0 * COUNT_W, 4 * COUNT_H, COUNT_W, COUNT_H * 2, "Committe", "Лицензионный коммитет", [0, 255, 255], "", "", "", "", 4)
    boxes.update({("Committe"): block})
    block = Box(0 * COUNT_W, 8 * COUNT_H, COUNT_W, COUNT_H * 2, "ShopOfProduct", "Сбыт", [0, 255, 255], "", "", "", "", 4)
    boxes.update({("ShopOfProduct"): block})
    block = Box(2 * COUNT_W, 9 * COUNT_H, COUNT_W * 2, COUNT_H, "Shop", "Рынок", [0, 255, 255], "", "", "", "", 4)
    boxes.update({("Shop"): block})
    block = Box(6 * COUNT_W, 9 * COUNT_H, COUNT_W * 2, COUNT_H, "Nalog", "Налоговая инспекция", [0, 255, 255], "", "", "", "", 4)
    boxes.update({("Nalog"): block})
    block = Box(4 * COUNT_W, 4 * COUNT_H, COUNT_W * 2, COUNT_H * 2, "Trade", "Трейд", [0, 255, 255], "", "", "", "", 4)
    boxes.update({("Trade"): block})
#=====Создание пустых блоков=====
    block = Box(0 * COUNT_W, 0 * COUNT_H, COUNT_W, COUNT_H, "empty0", "", [20, 20, 20], "", "", "", "", 0)
    boxes.update({("empty0"): block})
    block = Box(3 * COUNT_W, 0 * COUNT_H, COUNT_W * 2, COUNT_H, "empty1", "", [20, 20, 20], "", "", "", "", 0)
    boxes.update({("empty1"): block})
    block = Box(7 * COUNT_W, 0 * COUNT_H, COUNT_W * 2, COUNT_H, "empty2", "", [20, 20, 20], "", "", "", "", 0)
    boxes.update({("empty2"): block})
    block = Box(1 * COUNT_W, 9 * COUNT_H, COUNT_W, COUNT_H, "empty3", "", [20, 20, 20], "", "", "", "", 0)
    boxes.update({("empty3"): block})
    block = Box(4 * COUNT_W, 9 * COUNT_H, COUNT_W * 2, COUNT_H, "empty4", "", [20, 20, 20], "", "", "", "", 0)
    boxes.update({("empty4"): block})
    block = Box(8 * COUNT_W, 9 * COUNT_H, COUNT_W * 2, COUNT_H, "empty5", "", [20, 20, 20], "", "", "", "", 0)
    boxes.update({("empty5"): block})
    block = Box(0 * COUNT_W, 3 * COUNT_H, COUNT_W, COUNT_H, "empty6", "", [20, 20, 20], "", "", "", "", 0)
    boxes.update({("empty6"): block})
    block = Box(0 * COUNT_W, 6 * COUNT_H, COUNT_W, COUNT_H * 2, "empty7", "", [20, 20, 20], "", "", "", "", 0)
    boxes.update({("empty7"): block})
    block = Box(9 * COUNT_W, 2 * COUNT_H, COUNT_W, COUNT_H * 2, "empty8", "", [20, 20, 20], "", "", "", "", 0)
    boxes.update({("empty8"): block})
    block = Box(9 * COUNT_W, 6 * COUNT_H, COUNT_W, COUNT_H, "empty9", "", [20, 20, 20], "", "", "", "", 0)
    boxes.update({("empty9"): block})

    #=====Создание полей предприятий=====
    blocksName = ["Material", "HomeAppliances", "Cars", "Furniture", "Machines", "shopFurniture", "shopCars", "shopHomeAppliances", "shopMachines", "Hupermarket"]
    def createBox(boxName, number):
        id = boxName + str(number)
        name = boxName
        # print(name)
        x = data[id]["x_coordinate"]
        y = data[id]["y_coordonate"]
        color = data[id]["color"]
        blockType = data[id]["type"]
        resources = data[id]["resources"]
        pricePurchase = data[id]["pricePurchase"]
        priceSale = data[id]["priceSale"]
        production = data[id]["production"]
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
    for box in list(boxes):
        x = boxes.get(box).getX()
        y = boxes.get(box).getY()
        w = boxes.get(box).getW() + x
        h = boxes.get(box).getH() + y
        # print("Box searching: " + str(box))

        if (searchedX >= x and searchedX <= w and searchedY >= y and searchedY <= h):
            return box

def eventController(blockId):
    blockType = boxes.get(blockId).getBlockType()
    # print("blockId" + str(blockType))

    if (blockType == 0):
        print("event control")

        gameSession.nextPlayer()

        print(gameSession.course)
        print(gameSession.circle)
        print(gameSession.getCurretPlayer(gameSession.course))
        pass
    if (blockId == "Birsa"):
        # Main.players.get(curretPlayer).saleOfProduct()
        pass
    if (blockId == "Committe"):
        pass
    if (blockId == "ShopOfProduct"):
        pass
    if (blockId == "Shop"):
        # Main.players.get(gameSession.getCurretPlayer(gameSession.course)).purchaseCompany(company)
        pass
    if (blockId == "Nalog"):
        pass
    if (blockId == "Bank"):
        pass
    if (blockId == "Crysis"):
        pass
    if (blockId == "Ecology"):
        pass
    if (blockId == "ProductionOfProduct"):
        pass
    if (blockId == "ProductionOfMaterials"):
        pass
    if (blockId == "Trade"):
        pass

def writePlayerData():
    curretPlayer = gameSession.getCurretPlayer(gameSession.course)
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

def writeStatus():
    curretPlayer = gameSession.getCurretPlayer(gameSession.course)
    textPlayer = f.render("Игрок: " + curretPlayer, 1, (0, 0, 0))
    sc.blit(textPlayer, (20, 630))


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
while 1:

    sc.fill(white)
    clock.tick(60)
    # for i in range(int(COUNT_W)):
    #     for j in range(int(COUNT_W)):
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

