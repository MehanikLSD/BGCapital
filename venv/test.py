

class A:
    name = ""
    listA = None
    listB = []
    def __init__(self, name):
        self.name = name
        self.listA = dict()
        for n in range(5):
            self.listA.update({n:(name + str(n))})
            # listA = dict()
        for n in range(5):
            self.listB.append((name + str(n)))

objects = {}
for a in ["objA", "objB","objC","objD","objE"]:
    obj = A(a)
    objects.update({a:obj})

for o in list(objects):
    print(objects.get(o))
    print(objects.get(o).name)
    print(objects.get(o).listA)
    # print(objects.get(o).listB)
