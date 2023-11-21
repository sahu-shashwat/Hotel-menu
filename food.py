non_vegfood = {100:"chicken" ,  200:"mutton", 90:"fish", 80:"egg"}          
def cart(coll):
    print("your items")
    if "nonveg" in coll:
        for i in range(0, 1):
            print(
                coll[i].item1,
                coll[i].item2,
                coll[i].item3,
                coll[i].item4,
            )
    else:
        for i in range(0, 1):
            print(coll[i].item1, coll[i].item2, coll[i].item3, coll[i].item4)
    return "Now Enter Quantity"

def quantity(catch):
    l=[]
    if "nonveg" in catch:
        for i in range(0, 1):
           a= int(input(catch[i].item1))
           b= int(input(catch[i].item2))
           c= int(input(catch[i].item3))
           d= int(input(catch[i].item4))
           l+=[a,b,c,d]
    else:
        for i in range(0, 1):
           a= int(input(catch[i].item1))
           b= int(input(catch[i].item2))
           c= int(input(catch[i].item3))
           d= int(input(catch[i].item4))
           l+=[a,b,c,d]       
    k=0
    total=0
    for i in non_vegfood:
        a=i*l[k]
        total+=a
    print("Total bill",total)


class non_veg:
    rice = "Rice"

    def __init__(self, item1, item2, item3, item4):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4


class veg:
    chapati = "chapati"

    def __init__(self, item1, item2, item3, item4):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4

