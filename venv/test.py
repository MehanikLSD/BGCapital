class Massive:
    id = 0
    x = 0
    y = 0

    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def getID(self):
        return self.id

    def getX(self):
        return self.x

    def getY(self):
        return self.y

mass = {}
rang = 0
for i in range(20):
    m = Massive(i, rang, rang + 10)
    rang +=11
    mass.update({i:m})
    # print("mID: " + str(mass.get(i).getID()))
    # print("X: " + str(mass.get(i).getX()))
    # print("Y: " + str(mass.get(i).getY()))
    # print(" ")

def parsMess(n):
    for m in list(mass):
        qx = mass.get(m).getX()
        qy = mass.get(m).getY()
        if (n >= qx and n <= qy):
            return mass.get(m).getID()

myMass = parsMess(57)
if (myMass != None):
    print("My Massive: " + str(myMass))