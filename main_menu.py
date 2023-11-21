from food import veg, non_veg, cart, quantity

non_vegfood = {"chicken": 100, "mutton": 200, "fish": 90, "egg": 80, "prawn": 200}
veg_food = {"paneer": 150, "mushroom": 200, "gobi": 100, "soya": 90}

def select_items():
    choose = int(input("\n1)non-veg \n2)veg \nChoose:-"))
    l = []
    match choose:
        case 1:
            print(non_vegfood)

            l += [
                non_veg(
                    input("enter item1 "),
                    input("enter item2 "),
                    input("enter item3 "),
                    input("enter item4 "),
                ),
                "nonveg",
            ]
        case 2:
            print(veg_food)
            l += [
                veg(
                    input("enter item1 "),
                    input("enter item2 "),
                    input("enter item3 "),
                    input("enter item4 "),
                ),
                "veg",
            ]
    return l


def Home_page():
    print("WELLCOME")
    choose = int(
        input(
            "Menu:\n1)stater \n2)main_course \n3)dessert \n4)cold_drinks \n5)Exit \nChoose the Option:-"
        )
    )
    match choose:
        case 1:
            res = select_items()
            print(res)
            print(cart(res))
            quantity(res)
        case 2:
            print("maincourse")
        case 3:
            print("dessert")
        case 4:
            print("cold-drinks")
        case 5:
            exit()


Home_page()
